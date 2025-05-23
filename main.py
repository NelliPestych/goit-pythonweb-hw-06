from my_select import (
    list_all_subjects,
    list_all_teachers,
    list_all_students,
    list_all_groups,
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def run_all_queries():
    print("Subjects:", list_all_subjects())
    print("Teachers:", list_all_teachers())
    print("Students:", list_all_students())
    print("Groups:", list_all_groups())

    print("1. Top 5 students with highest average grade:")
    print(select_1())
    print()

    print("2. Student with highest average grade in a subject:")
    print(select_2("Banker"))
    print()

    print("3. Average grade in groups for a specific subject:")
    print(select_3("Retail merchandiser"))
    print()

    print("4. Average grade for the whole stream:")
    print(select_4())
    print()

    print("5. Courses taught by a specific teacher:")
    print(select_5("Ryan Watts"))
    print()

    print("6. List of students in a specific group:")
    print(select_6("Group 1"))
    print()

    print("7. Grades of students in a group by subject:")
    print(select_7("Group 1", "Press sub"))
    print()

    print("8. Average grade given by a teacher:")
    print(select_8("Kevin Barnes"))
    print()

    print("9. Courses attended by a student:")
    print(select_9("Megan Carpenter"))
    print()

    print("10. Courses a teacher teaches to a student:")
    print(select_10("Eric Anderson", "Brianna Larsen"))
    print()


if __name__ == "__main__":
    run_all_queries()