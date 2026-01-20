#5.WAP to demonstrate pickling process without file and with file using pickledump() and pickleload() functions.
import pickle
data=["apple", "banana", "mango"]
pickled=pickle.dumps(data)
print(pickled)

unpickled=pickle.loads(pickled)
print(unpickled) 
#6.	Write a Python program that defines a dictionary containing some data (e.g., student information, employee records, etc.).
# Define a dictionary containing student information
#a.	Use the pickle module to serialize (i.e., convert) the dictionary into a binary file.
#b.	Write a function that reads the serialized binary file using pickle and returns the deserialized (i.e., converted back to its original form) dictionary.
#c.	Test your program by serializing the dictionary, writing it to a file, reading the file using the function, and printing the deserialized dictionary.
# Define the dictionary containing student information
student_info = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "grades": {"Math": "A", "Physics": "B+", "Chemistry": "A-"}
}

# Serialize the dictionary and write it to a binary file
with open("student_info.pkl", "wb") as file:
    pickle.dump(student_info, file)

# Function to read the serialized binary file and return the deserialized dictionary
def read_student_info(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)

# Test the function
deserialized_info = read_student_info("student_info.pkl")
print("Deserialized Student Information:")
print(deserialized_info)

# Print the dictionary
print("Student Information:")
print(student_info)


