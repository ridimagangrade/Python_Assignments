import csv

counter = 0

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        counter += 1

print(f"The number of rows are: {counter}")

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)