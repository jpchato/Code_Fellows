"""
Feature Tasks
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.
Example
Input	Output
[1, 2, 3, 4, 5, 6]	[6, 5, 4, 3, 2, 1]
[89, 2354, 3546, 23, 10, -923, 823, -12]	[-12, 823, -923, 10, 23, 3546, 2354, 89]

"""

def reverse_array(input_list):
    return input_list[::-1]

print(reverse_array([1, 2, 3, 4, 5, 6]))
print(reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12]))
