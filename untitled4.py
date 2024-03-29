# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17yk63M8F_yg8D7yrXJYvd2k4SOYUV0Ru
"""

file_path = 'log.txt'  # Replace 'your_file.txt' with the path to your file
variable_list = []

try:
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line by tab spaces ('\t')
            values = line.strip().split('\t')
            # Add the split values to the variable_list
            variable_list.append(values)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# Display the content of the variable_list
print("Content of variable_list:")
external_string_array = []
for item in variable_list:
    print(item)

output_array = []

for sublist in variable_list:
    if len(sublist) >= 3:  # Checking if sublist has at least three elements
        output_array.append([sublist[2]])

# Display the output array
print("Output array:")
# Desired strings to count

# for class A finding
strings_to_count = ['ldd', 'lwd', 'lwud','sdd','swd']

total_count = 0
# Iterate through each sublist and count occurrences of desired strings
for sublist in output_array:
    for string in sublist:
        if string in strings_to_count:
            total_count += 1

# Display the total count
print("Total count of found variables:", total_count)


# for class B finding
strings_to_count_fld = ['fld']

total_count_fld = 0
# Iterate through each sublist and count occurrences of desired strings
for sublist in output_array:
    for string in sublist:
        if string in strings_to_count_fld:
            total_count_fld += 1

# Display the total count
print("class thead instruction:", total_count)
print("Class fload Instruction:", total_count_fld)

from google.colab import drive
drive.mount('/content/drive')