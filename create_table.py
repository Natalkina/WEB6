from connection import create_connection


def create_table(conn, sql_execute):
    try:
        c = conn.cursor()
        c.execute(sql_execute)
        c.close()
        conn.commit()
    except Exception as err:
        print(err)


if __name__ == "__main__":

    sql_groups = """
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(60),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    sql_students = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(60),
        group_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (group_id) REFERENCES groups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
    """
    sql_teachers = """
    CREATE TABLE IF NOT EXISTS teachers (
        id  SERIAL PRIMARY KEY,
        name VARCHAR(60),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    sql_subjects = """
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(60),
            teacher_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        );
        """
    sql_rating = """
            CREATE TABLE IF NOT EXISTS rating (
                id SERIAL PRIMARY KEY,
                value INTEGER,
                student_id INTEGER,
                subject_id INTEGER,
                date_of DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (subject_id) REFERENCES subjects (id),
                FOREIGN KEY (student_id) REFERENCES students (id)
                
            );
            """

    with create_connection() as conn:
        create_table(conn, sql_groups)
        create_table(conn, sql_students)
        create_table(conn, sql_teachers)
        create_table(conn, sql_subjects)
        create_table(conn, sql_rating)
        c = conn.cursor()

        c.close()
        conn.commit()

