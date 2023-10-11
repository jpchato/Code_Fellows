"""
Feature Tasks
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
Example
Input	Output
[2,4,6,-8], 5	[2,4,5,6,-8]
[42,8,15,23,42], 16	[42,8,15,16,23,42]

"""

def shift_array_insert(input_array, value_to_be_added):
    length = len(input_array)
    halfway_point = length // 2

    # Handle the case for an empty array
    if length == 0:
        return [value_to_be_added]
    
    # Handle even and odd lengths differently
    if length % 2 == 0:
        left_array = input_array[:halfway_point]
        right_array = input_array[halfway_point:]
    else:
        left_array = input_array[:halfway_point + 1]
        right_array = input_array[halfway_point + 1:]

    output_array = left_array + [value_to_be_added] + right_array
    return output_array

# Testing the function
print(shift_array_insert([2, 4, 6, -8], 5))  # Output: [2, 4, 5, 6, -8]
print(shift_array_insert([42, 8, 15, 23, 42], 16))  # Output: [42, 8, 15, 16, 23, 42]
print(shift_array_insert([], 5))  # Output: [5]
print(shift_array_insert([1], 5))  # Output: [1, 5]
