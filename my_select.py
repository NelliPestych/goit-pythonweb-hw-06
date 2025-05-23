from sqlalchemy import select, func, desc, Numeric
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import Student, Grade, Subject, Teacher, Group

def list_all_subjects():
    with SessionLocal() as session:
        return [subject.name for subject in session.query(Subject).all()]

def list_all_teachers():
    with SessionLocal() as session:
        return [teacher.name for teacher in session.query(Teacher).all()]

def list_all_students():
    with SessionLocal() as session:
        return [student.name for student in session.query(Student).all()]

def list_all_groups():
    with SessionLocal() as session:
        return [group.name for group in session.query(Group).all()]

# 1. 5 студентів з найвищим середнім балом
def select_1():
    with SessionLocal() as session:
        result = (
            session.query(Student.name, func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade"))
            .join(Grade)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )
        return result

# 2. Студент з найвищим середнім балом з певного предмета
def select_2(subject_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Student.name, func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade"))
            .join(Grade)
            .join(Subject)
            .filter(Subject.name == subject_name)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .first()
        )
        return result

# 3. Середній бал у групах з певного предмета
def select_3(subject_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Group.name, func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade"))
            .select_from(Student)
            .join(Group)
            .join(Grade)
            .join(Subject)
            .filter(Subject.name == subject_name)
            .group_by(Group.id)
            .all()
        )
        return result

# 4. Середній бал на потоці
def select_4():
    with SessionLocal() as session:
        result = session.query(func.round(func.avg(Grade.grade).cast(Numeric), 2)).scalar()
        return result

# 5. Курси, які читає певний викладач
def select_5(teacher_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Subject.name)
            .join(Teacher)
            .filter(Teacher.name == teacher_name)
            .all()
        )
        return result

# 6. Список студентів у певній групі
def select_6(group_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Student.name)
            .join(Group)
            .filter(Group.name == group_name)
            .all()
        )
        return result

# 7. Оцінки студентів у певній групі з певного предмета
def select_7(group_name: str, subject_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Student.name, Grade.grade)
            .join(Group)
            .join(Grade)
            .join(Subject)
            .filter(Group.name == group_name, Subject.name == subject_name)
            .all()
        )
        return result

# 8. Середній бал, який ставить певний викладач
def select_8(teacher_name: str):
    with SessionLocal() as session:
        result = (
            session.query(func.round(func.avg(Grade.grade).cast(Numeric), 2))
            .join(Subject)
            .join(Teacher)
            .filter(Teacher.name == teacher_name)
            .scalar()
        )
        return result

# 9. Курси, які відвідує певний студент
def select_9(student_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Subject.name)
            .join(Grade)
            .join(Student)
            .filter(Student.name == student_name)
            .distinct()
            .all()
        )
        return result

# 10. Курси, які певному студенту читає певний викладач
def select_10(student_name: str, teacher_name: str):
    with SessionLocal() as session:
        result = (
            session.query(Subject.name)
            .join(Grade)
            .join(Student)
            .join(Teacher)
            .filter(Student.name == student_name, Teacher.name == teacher_name)
            .distinct()
            .all()
        )
        return result
