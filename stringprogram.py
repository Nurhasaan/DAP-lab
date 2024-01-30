#Python Program to find the sum of an array:

def array_sum(arr):
    return sum(arr)

# Example usage:
arr = [1, 2, 3, 4, 5]
print("Sum of array:", array_sum(arr))

#Python Program to find the largest element in an array:

def find_largest_element(arr):
    return max(arr)

# Example usage:
arr = [5, 2, 9, 1, 7]
print("Largest element in array:", find_largest_element(arr))


#Python Program for array rotation:

def rotate_array(arr, k):
    return arr[k:] + arr[:k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated array:", rotate_array(arr, k))


#Python Program for Reversal algorithm for array rotation:

def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, k):
    n = len(arr)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated array:", rotate_array_reversal(arr, k))


#Python Program to Split the array and add the first part to the end:

def split_and_add(arr, k):
    return arr[k:] + arr[:k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print("Modified array:", split_and_add(arr, k))


#Python Program for Find reminder of array multiplication divided by n:

def array_mul_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

# Example usage:
arr = [2, 3, 4]
n = 5
print("Reminder of array multiplication divided by n:", array_mul_remainder(arr, n))


#Python Program to check if the given array is Monotonic:

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

# Example usage:
arr = [1, 2, 3, 4, 5]
print("Is the array monotonic?", is_monotonic(arr))


#
