students = {}

number = int(input("Enter number of students: "))

for i in range(number):
    print(f"\nStudent {1 + i}")
    name = input("Enter name: ")
    grade1 = float(input("Enter grade1: "))
    grade2 = float(input("Enter grade2: "))
    grade3 = float(input("Enter grade3: "))
    students[name] = [grade1, grade2, grade3]

print("\n===== STUDENT RECORD =====")
for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average:", round(average, 2))

highest = 0
namehighest = ""
tally = 0

print("\n===== SUMMARY =====")

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, "Average:", round(average, 2))
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally += 1

print(f"\nStudent {namehighest} got the highest average: {round(highest, 2)}")
print(f"There are {tally} grades which are below 75.")
