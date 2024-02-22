class Student:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Date of Birth: {self.dob}"

    @staticmethod
    def input():
        name = input("Please enter student's name: ")
        age = input("Please enter student's age: ")
        dob = input("Please input student's date of birth: ")
        return Student(name, age, dob)


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def __str__(self):
        return f"Course Name: {self.name}, Course ID: {self.course_id}"

    @staticmethod
    def input():
        course_name = input("Please enter course's name: ")
        course_id = input("Please enter course's id: ")
        return Course(course_name, course_id)


class Mark:
    def __init__(self, marks):
        self.marks = marks

    def __str__(self):
        return f"Marks: {self.marks}"

    @staticmethod
    def input():
        marks = float(input("Please input student's marks: "))
        return Mark(marks)


class DataCollection:
    @staticmethod
    def input_number(prompt):
        return int(input(prompt))

    @staticmethod
    def list_info(items):
        for item in items:
            print(item)


def main():
    data_collection = DataCollection()

    num_students = data_collection.input_number(
        "Please enter a number of students: ")
    students_info = [Student.input() for _ in range(num_students)]

    num_courses = data_collection.input_number(
        "Please enter a number of courses: ")
    courses_info = [Course.input() for _ in range(num_courses)]

    marks_info = [Mark.input() for _ in range(num_students)]

    print("\nStudents Information:")
    data_collection.list_info(students_info)

    print("\nCourses Information:")
    data_collection.list_info(courses_info)

    print("\nMarks Information:")
    data_collection.list_info(marks_info)


if __name__ == "__main__":
    main()
