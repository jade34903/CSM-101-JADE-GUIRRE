students = {
    "Ana" : 85,
    "Bob" : 80,
    "Charlie" : 80,
    "David" : 80,
}
print("STUDENT GRADE")
print("------------------------")
print("Ana: ", students["Ana"])
print("Bob: ", students["Bob"])
# Add new student
students["Ella"] = 88
# Update a student's grade
students["Charlie"] = 80
students["David"] = 91
name1 = input("Enter student name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdated student grade")
print("-------------------------")
for name, grade in students.items():
    print(name, ":", grade)

search = input("\nEnter student name to search: ")

if search in students:
    print(search, "has a grade of ", students[search])
else:
    print("Student not found")