

import os
import csv

#Set your folder path here
folder_path = r"C:\\Users\\ved parmar\\OneDrive\\Desktop\\python"  # Change this to your own folder path

# Create new folder
os.makedirs(folder_path, exist_ok=True)

# Define full file paths
txt_file_path = os.path.join(folder_path, "file.txt")
csv_file_path = os.path.join(folder_path, "file.csv")

# -------- TXT FILE OPERATIONS --------

# Write initial content to the .txt file (creates or overwrites)
with open(txt_file_path, "w") as f:
    f.write("Hello from text file!\n")

# Append the required line to the existing .txt file
with open(txt_file_path, "a") as f:
    f.write("Hello World! I am using python\n")

# Read and print contents of the .txt file
with open(txt_file_path, "r") as f:
    print("Contents of file.txt:")
    print(f.read())

# -------- CSV FILE OPERATIONS --------

# Write headers and rows to the .csv file (creates or overwrites)
with open(csv_file_path, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No.", "Name", "Department", "Course"])
    writer.writerow(["11021", "Mahek", "CSE", "Python"])
    writer.writerow(["11022", "Heer", "ICT", "Mathematics"])
    writer.writerow(["11023", "Pavan", "CIE", "Physics"])
    writer.writerow(["11024", "Moksh", "ICT", "Data Structure"])

# Read and print contents of the .csv file
with open(csv_file_path, "r") as file:
    reader = csv.reader(file)
    print("\nContents of file.csv:")
    for row in reader:
        print(row)

# Step 1: Create 'input.txt' and write some text to it
with open("input.txt", "w") as input_file:
    input_file.write("This is a sample text file.\n")
    input_file.write("It contains multiple lines of text.\n")
    input_file.write("We are learning file handling in Python.")

# Step 2: Open 'input.txt' for reading
with open("input.txt", "r") as input_file:
    # Step 3: Read contents
    content = input_file.read()
    print("Contents of input.txt:")
    print(content)

# Step 4: Open 'output.txt' for writing
with open("output.txt", "w") as output_file:
    # Step 5: Write the read content into 'output.txt'
    output_file.write(content)

# Files are automatically closed after the with-block