class Student:
    count = 1000

    def __init__(self, name):
        self.id = Student.count
        Student.count += 1
        self.name = name
        self.courses = []
        self.balance = 100

    def enroll_course(self, course):
        self.courses.append(course)

    def view_balance(self):
        print(f"Balance for {self.name}: ${self.balance}")

    def pay_fees(self, amount):
        print(f"${amount} fees paid successfully for {self.name}")
        self.balance -= amount
        print(f"Remaining balance: ${self.balance}")

    def show_status(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Balance: ${self.balance}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student {name} added successfully. Student ID: {student.id}")

    def find_student(self, student_id):
        return next((s for s in self.students if s.id == student_id), None)

    def enroll_student(self, student_id, course):
        student = self.find_student(student_id)
        if student:
            student.enroll_course(course)
            print(f"Student {student.name} enrolled in {course} successfully!")
        else:
            print("Student not found.")

    def view_student_balance(self, student_id):
        student = self.find_student(student_id)
        if student:
            student.view_balance()
        else:
            print("Student not found. Enter a correct student ID.")

    def pay_student_fees(self, student_id, amount):
        student = self.find_student(student_id)
        if student:
            student.pay_fees(amount)
        else:
            print("Student not found. Enter a correct student ID.")

    def show_student_status(self, student_id):
        student = self.find_student(student_id)
        if student:
            student.show_status()
        else:
            print("Student not found. Enter a correct student ID.")


def main():
    print("Welcome to OOP Program University Enrollment System")
    print("-" * 50)

    student_manager = StudentManager()

    while True:
        print("\nSelect an operation:")
        print("1. Add Student")
        print("2. Enroll Student in a Course")
        print("3. View Student Balance")
        print("4. Pay Fees")
        print("5. Show Student Status")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            student_manager.add_student(name)

        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                course = input("Enter course name: ")
                student_manager.enroll_student(student_id, course)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")

        elif choice == '3':
            try:
                student_id = int(input("Enter student ID: "))
                student_manager.view_student_balance(student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")

        elif choice == '4':
            try:
                student_id = int(input("Enter student ID: "))
                amount = int(input("Enter the amount to pay: "))
                student_manager.pay_student_fees(student_id, amount)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == '5':
            try:
                student_id = int(input("Enter student ID: "))
                student_manager.show_student_status(student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")

        elif choice == '6':
            print("Exiting the System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
