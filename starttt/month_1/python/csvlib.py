import csv
hogwarts=[]
with open(r"C:\Users\exact\OneDrive\Desktop\student portal\node_modules\flatted\python\starttt\month_1\python\hogwarts.csv") as file:
    reader= csv.reader(file)
    for name, home in reader:
        hogwarts.append({"name": name, "home": home})
for student in sorted(hogwarts, key=lambda student: student["name"]):
     print(f"{student['name']} is from {student['home']}")