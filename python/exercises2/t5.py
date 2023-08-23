number_of_students = int(input("Enter the number of students: "))

students = {}

for i in range(number_of_students):
    name, *grades = input("Enter the name and grades of the student (space-separated): ").split()
    grades = [int(grade) for grade in grades]
    students[name] = sum(grades) / len(grades)

student_name = input("Enter the name of the student whose average you want to find: ")

print(f"The average of {student_name} is {students[student_name]}")
