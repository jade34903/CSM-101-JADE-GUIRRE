students = {
    "Ana": [90, 85, 82],
    "Bob": [72, 75, 78],
    "Charlie": [89, 69, 81],
}

highest = 0
namehighest = ""
lowest = float('inf')
namelowest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print(f"student {namehighest} got the highest grade: {highest:.2f}")
print(f"student {namelowest} got the lowest grade: {lowest:.2f}")
print(f"There are {tally} grades which are below 75.")
