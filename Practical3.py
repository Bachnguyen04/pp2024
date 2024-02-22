import math


class Student:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob
        self.marks = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Date of Birth: {self.dob}, Average GPA: {self.calculate_avg_gpa()}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def calculate_avg_gpa(self):
        if not self.marks:
            return 0
        total_gpa = sum(mark.marks for mark in self.marks) / len(self.marks)
        return round(total_gpa, 1)


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def __str__(self):
        return f"Course Name: {self.name}, Course ID: {self.course_id}"


class Mark:
    def __init__(self, marks):
        self.marks = math.floor(marks * 10) / 10

    def __str__(self):
        return f"Marks: {self.marks}"


def input_number(prompt):
    return int(input(prompt))


def list_info(items):
    for item in items:
        print(item)


def input_student_info(student_num):
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd"}
    if student_num in (1, 2, 3):
        suffix = ordinal_suffix[student_num]
    else:
        suffix = "th"
    name = input(f"Please enter the {student_num}{suffix} student's name: ")
    age = input(f"Please enter the {student_num}{suffix} student's age: ")
    dob = input(
        f"Please input the {student_num}{suffix} student's date of birth: ")
    return Student(name, age, dob)


def input_course_info(course_num):
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd"}
    if course_num in (1, 2, 3):
        suffix = ordinal_suffix[course_num]
    else:
        suffix = "th"
    course_name = input(
        f"Please enter the {course_num}{suffix} course's name: ")
    course_id = input(f"Please enter the {course_num}{suffix} course's id: ")
    return Course(course_name, course_id)


def input_marks(student_num, course_num):
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd"}
    if student_num in (1, 2, 3):
        student_suffix = ordinal_suffix[student_num]
    else:
        student_suffix = "th"
    if course_num in (1, 2, 3):
        course_suffix = ordinal_suffix[course_num]
    else:
        course_suffix = "th"
    marks = float(input(
        f"Please input the {student_num}{student_suffix} student's marks for the {course_num}{course_suffix} course: "))
    return Mark(marks)


def main():
    num_students = input_number("Please enter a number of students: ")
    students_info = [input_student_info(i+1) for i in range(num_students)]

    num_courses = input_number("Please enter a number of courses: ")
    courses_info = [input_course_info(i+1) for i in range(num_courses)]

    for student_num, student in enumerate(students_info, start=1):
        for course_num in range(1, num_courses + 1):
            mark = input_marks(student_num, course_num)
            student.add_mark(mark)

    print("\nStudents Information:")
    list_info(students_info)

    print("\nCourses Information:")
    list_info(courses_info)


if __name__ == "__main__":
    main()
