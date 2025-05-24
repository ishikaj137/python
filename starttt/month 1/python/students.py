with open("C:/Users/exact/OneDrive/Desktop/student portal/node_modules/flatted/python/starttt/month 1/python/student.csv") as file: #func to open csv
    for line in file:
        name,city= line.rstrip().split(",")
        print(f"{name} lives in {city}")
