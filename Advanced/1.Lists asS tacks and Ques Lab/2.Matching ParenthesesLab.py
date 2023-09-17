n = int(input())

students = {}

for i in range(n):
    name, grade = input().split()

    if name not in students:
        students[name]=[float(grade)]
        continue
    students[name].append(float(grade))


for student,grade in students.items():
    avg = sum(grade) / len(grade)

    print(f"{student} -> {' '.join(str(f'{x:.2f}') for x in grade)} (avg: {avg:.2f})")