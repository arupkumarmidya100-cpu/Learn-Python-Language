students = {
    "Arup": 90,
    "Rahul": 45,
    "Sourav": 95,
    "Amit": 40
}

count = 0

for marks in students.values():
    if marks > 50:
        count += 1

print("Students scored more than 50:", count)