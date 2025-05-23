import random
from datetime import date, timedelta
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Group, Student, Teacher, Subject, Grade

fake = Faker()
engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()

# Create groups
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)

# Create teachers
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)

# Create subjects
subjects = [Subject(name=fake.job(), teacher=random.choice(teachers)) for _ in range(6)]
session.add_all(subjects)

# Create students
students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]
session.add_all(students)
session.commit()

# Create grades
grades = []
for student in students:
    for subject in subjects:
        for _ in range(random.randint(2, 5)):
            grade = Grade(
                student=student,
                subject=subject,
                date_received=fake.date_between(start_date='-1y', end_date='today'),
                grade=round(random.uniform(60, 100), 2)
            )
            grades.append(grade)

session.add_all(grades)
session.commit()

print("Database seeded successfully.")
