def input_number_of_students():
    return int(input("Please enter a number of students: "))


def input_student_info():
    name = input("Please enter student's name: ")
    age = input("Please enter student's age: ")
    dob = input("Please input student's date of birth: ")
    return {"Name": name, "Age": age, "DoB": dob}


def input_number_of_courses():
    return int(input("Please enter a number of courses: "))


def input_course_info():
    course_name = input("Please enter course's name: ")
    id = input("Please enter course's id: ")
    return {"Course's name": course_name, "Course's id": id}


def input_marks():
    marks = float(input("Please input student's marks: "))
    return {"Marks": marks}


def main():
    num_students = input_number_of_students()
    students_info = []

    for i in range(num_students):
        student_info = input_student_info()
        students_info.append(student_info)

    num_courses = input_number_of_courses()
    courses_info = []

    for i in range(num_courses):
        course_info = input_course_info()
        courses_info.append(course_info)

    marks_info = []
    for i in range(num_students):
        mark_info = input_marks()
        marks_info.append(mark_info)

    print("\nStudents Information:")
    print(students_info)

    print("\nCourses Information:")
    print(courses_info)

    print("\nMarks Information:")
    print(marks_info)


main()
