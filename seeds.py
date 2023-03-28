from datetime import datetime, date, timedelta
from random import randint
from typing import List
from connection import create_connection
from faker import Faker

fake = Faker('uk-UA')

subjects = [
    "Теорія електричних кіл",
    "Ймовірнісні основи обробки даних",
    "Математичний аналіз",
    "Основи схемотехніки",
    "Аналітична геометрія",
    "Вступ до програмувавання на Python",
    "Прикладна механіка",
    "Цифрова обробка процесів",
    "Основи електроніки"
]

groups = ['А-01', 'А-02', 'А-03']

NUMBERS_TEACHERS = 6
NUMBER_STUDENTS = 60


def seed_teacher(cur):
    teachers = [fake.name() for _ in range(NUMBERS_TEACHERS)]
    teachers_id = range(1, NUMBERS_TEACHERS+1)
    sql_ex = "INSERT INTO teachers(name, id) VALUES(%s, %s);"
    cur.executemany(sql_ex, zip(teachers, teachers_id))


def seed_groups(cur):
    groups_id = range(1, len(groups)+1)
    sql_ex = "INSERT INTO groups(name, id) VALUES(%s, %s);"
    cur.executemany(sql_ex, zip(groups, groups_id))


def seed_subjects(cur):
    subjects_id = range(1, len(subjects) + 1)
    list_teacher_id = [randint(1, NUMBERS_TEACHERS) for _ in range(len(subjects))]
    sql_ex = "INSERT INTO subjects(name, teacher_id, id) VALUES(%s, %s, %s);"
    cur.executemany(sql_ex, zip(subjects, iter(list_teacher_id), subjects_id))


def seed_students(cur):
    students_id = range(1, NUMBER_STUDENTS + 1)
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBER_STUDENTS)]
    sql_ex = "INSERT INTO students(name, group_id, id) VALUES(%s, %s, %s);"
    cur.executemany(sql_ex, zip(students, iter(list_group_id), students_id))


def seed_grades(cur):
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")


    sql_ex = "INSERT INTO rating(value, student_id, subject_id, date_of) VALUES(%s, %s, %s, %s);"

    def get_list_of_date(start_date, end_date) -> List[date]:
        result = []
        current_date: date = start_date
        while current_date <= end_date:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_of_date(start_date, end_date)

    grades = []

    for day in list_dates:

        random_subject = randint(1, len(subjects))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((randint(1, 12), student, random_subject, day.date()))
    cur.executemany(sql_ex, grades)


if __name__ == '__main__':
    with create_connection() as conn:
        cur = conn.cursor()
        seed_teacher(cur)
        seed_groups(cur)
        seed_subjects(cur)
        seed_students(cur)
        seed_grades(cur)
        conn.commit()
        conn.close()