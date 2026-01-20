
import csv
# Open and read the existing .txt file
with open("sample.txt", "r") as file:
    print(file.read())

# Open the same file and add a new line
with open("sample.txt", "a") as file:
    file.write()

# Read again to see the updated content
with open("sample.txt", "r") as file:
    updated = file.read()
    print(updated)
filepath = "sample.txt"
rows = [
    ["Roll No.", "Name", "Department", "Course"],
    [11021, "Mahek", "CSE", "Python"],
    [11022, "Heer", "ICT", "Mathematics"],
    [11023, "Pavan", "CIE", "Physics"],
    [11024, "Moksh", "ICT", "Data Structure"]
]

# Open CSV file and append data
with open("stuti.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read and display CSV file content
with open("stuti.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)