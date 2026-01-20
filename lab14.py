#1.Write a NumPy program to create a 3X4 array and iterate over it.
import numpy as np
arr= np.arange(12).reshape(3, 4)
print("3X4 array:")
print(arr)
print("Iterating over the array:")
for row in arr:
    for element in row:
        print(element, end=" ")
    print()

#2.	Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
arr = np.arange(10, 22).reshape(3, 4)
print("3x4 matrix filled with values from 10 to 21:")
print(arr)

#3.	Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
arr = np.zeros((10, 10), dtype=int)
arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1
print("10x10 matrix with borders equal to 1 and inside 0:")
print(arr)

#4.Write a Python function that takes two 2D arrays as input and returns their matrix product using NumPy.
def matrix_product(arr1, arr2):
    return np.dot(arr1, arr2)

#5.Write a Python function that takes a 1D NumPy array as input and returns 
# a new array with all even numbers squared and odd numbers unchanged.
def square_even_numbers(arr):
    return np.where(arr % 2 == 0, arr ** 2, arr)

#6.	Write a NumPy program to compute the sum of all elements, 
# the sum of each column and the sum of each row in a given array.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
total_sum = np.sum(arr)
column_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)
print("Total sum of all elements:", total_sum)
print("Sum of each column:", column_sum)
print("Sum of each row:", row_sum)

#7.Write a NumPy program to add a vector to each row of a given matrix.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 2, 3])
result = arr + vector
print("Matrix after adding vector to each row:")
print(result)

#8.Consider a given series: 
#QTR1	50000
#QTR2	65890
#QTR3	56780
#QTR4	89000
#QTR5	77900
#Write a program in Python Pandas to create and display the series.
import pandas as pd
data = {
    'QTR1': 50000,
    'QTR2': 65890,
    'QTR3': 56780,
    'QTR4': 89000,
    'QTR5': 77900
}
series = pd.Series(data)
print("Series:")
print(series)

#9.Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd
# Create two Pandas Series
series1 = pd.Series([10, 20, 30, 40])
series2 = pd.Series([1, 2, 3, 4])

# Perform addition, subtraction, multiplication, and division
addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2
print("Addition:")
print(addition)
print("Subtraction:")
print(subtraction)
print("Multiplication:")
print(multiplication)
print("Division:")
print(division)

#10.Write a Pandas program to convert given series into a dataframe with its index as another column on the dataframe.
import pandas as pd
# Create a Pandas Series
series = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
# Convert the Series into a DataFrame
df = series.reset_index()
df.columns = ['Index', 'Value']
print("DataFrame:")
print(df)

#11.Write a Pandas program to iterate over rows in a DataFrame.
import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

#12.Write a Pandas program to rename columns of a given DataFrame.
import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Rename columns
df.rename(columns={'Name': 'Full Name', 'Age': 'Years', 'City': 'Location'}, inplace=True)
print("DataFrame with renamed columns:")
print(df)

#13.Write a Pandas program to add one row in an existing DataFrame.
import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Add a new row
new_row = pd.DataFrame({'Name': ['David'], 'Age': [28], 'City': ['San Francisco']})
df = pd.concat([df, new_row], ignore_index=True)
print("DataFrame after adding a new row:")
print(df)

#14.Write a Pandas program to write a DataFrame to CSV file using tab separator.
import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Write the DataFrame to a CSV file using tab separator
df.to_csv('data.tsv', sep='\t', index=False)

#15.Write a Pandas program to find the row for where the value of a given column is maximum.
import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Find the row where the value of the 'Age' column is maximum
max_row = df.loc[df['Age'].idxmax()]
print("Row with maximum value in 'Age' column:")
print(max_row)


