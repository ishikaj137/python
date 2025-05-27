students = []
with open(r"C:\Users\exact\OneDrive\Desktop\student portal\node_modules\flatted\python\starttt\month_1\python\students.csv") as file: #func to open csv
    for line in file:
        name,city= line.rstrip().split(",")
        students.append({"name":name, "city":city})
def get_city(student):
     return student["city"]
for student in sorted(students, key=get_city):
    print(f"{student['name']} lives in {student['city']}")