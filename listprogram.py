#Python program to interchange first and last elements in a list:

def interchange_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Interchanged list:", interchange_first_last(my_list))
#Python program to swap two elements in a list:
def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
pos1, pos2 = 1, 3
print("Swapped list:", swap_elements(my_list, pos1, pos2))
#Python | Ways to find the length of a list:
def find_list_length(lst):
    return len(lst)

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Length of the list:", find_list_length(my_list))
#Python | Ways to check if an element exists in a list:
def element_exists(lst, element):
    return element in lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
element_to_check = 3
print(f"Does {element_to_check} exist in the list? {element_exists(my_list, element_to_check)}")
#Different ways to clear a list in Python:
def clear_list(lst):
    lst.clear()
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Cleared list:", clear_list(my_list))
#Python | Reversing a List:
def reverse_list(lst):
    return lst[::-1]

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(my_list))

#Python program to find the sum of elements in a list:

def sum_of_elements(lst):
    return sum(lst)

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Sum of elements in the list:", sum_of_elements(my_list))
#Python | Multiply all numbers in the list:

def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Product of all numbers in the list:", multiply_elements(my_list))
#Python program to find the smallest number in a list:

def find_smallest_number(lst):
    return min(lst)

# Example usage:
my_list = [5, 2, 9, 1, 7]
print("Smallest number in the list:", find_smallest_number(my_list))
#Python program to find the largest number in a list:

def find_largest_number(lst):
    return max(lst)

# Example usage:
my_list = [5, 2, 9, 1, 7]
print("Largest number in the list:", find_largest_number(my_list))
#Python program to find the second-largest number in a list:

def find_second_largest(lst):
    sorted_list = sorted(set(lst), reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else "No second-largest element"

# Example usage:
my_list = [5, 2, 9, 1, 7]
print("Second largest number in the list:", find_second_largest(my_list))
#Python program to find N largest elements from a list:

def find_n_largest_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

# Example usage:
my_list = [5, 2, 9, 1, 7]
n = 3
print(f"{n} largest elements in the list:", find_n_largest_elements(my_list, n))
#Python program to print even numbers in a list:

def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Even numbers in the list:", print_even_numbers(my_list))
#Python program to print odd numbers in a List:

def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Odd numbers in the list:", print_odd_numbers(my_list))
#Python program to print all even numbers in a range:

def print_even_numbers_in_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

# Example usage:
start, end = 1, 10
print(f"All even numbers in the range {start} to {end}:", print_even_numbers_in_range(start, end))
#Python program to print all odd numbers in a range:

def print_odd_numbers_in_range(start, end):
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    return odd_numbers

# Example usage:
start, end = 1, 10
print(f"All odd numbers in the range {start} to {end}:", print_odd_numbers_in_range(start, end))
#Python program to print positive numbers in a list:

def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers

# Example usage:
my_list = [-1, 2, -3, 4, -5]
print("Positive numbers in the list:", print_positive_numbers(my_list))
#Python program to print negative numbers in a list:

def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers

# Example usage:
my_list = [-1, 2, -3, 4, -5]
print("Negative numbers in the list:", print_negative_numbers(my_list))
#Python program to print all positive numbers in a range:

def print_positive_numbers_in_range(start, end):
    positive_numbers = [num for num in range(start, end + 1) if num > 0]
    return positive_numbers

# Example usage:
start, end = -5, 5
print(f"All positive numbers in the range {start} to {end}:", print_positive_numbers_in_range(start, end))
#Python program to print all negative numbers in a range:

def print_negative_numbers_in_range(start, end):
    negative_numbers = [num for num in range(start, end + 1) if num < 0]
    return negative_numbers

# Example usage:
start, end = -5, 5
print(f"All negative numbers in the range {start} to {end}:", print_negative_numbers_in_range(start, end))
#Remove multiple elements from a list in Python:

def remove_elements(lst, elements_to_remove):
    return [element for element in lst if element not in elements_to_remove]

# Example usage:
my_list = [1, 2, 3, 4, 5]
elements_to_remove = [2, 4]
print("List after removing elements:", remove_elements(my_list, elements_to_remove))
#Python – Remove empty List from List:

def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

# Example usage:
my_list = [1, [], 3, [], 5, [], 7]
print("List after removing empty lists:", remove_empty_lists(my_list))
#Python | Cloning or Copying a list:

def clone_list(lst):
    return lst.copy()

# Example usage:
my_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(my_list)
print("Original list:", my_list)
print("Cloned list:", cloned_list)
#Python | Count occurrences of an element in a list:

def count_occurrences(lst, element):
    return lst.count(element)

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_count = 2
print(f"Number of occurrences of {element_to_count} in the list:", count_occurrences(my_list, element_to_count))
#Python | Remove empty tuples from a list:

def remove_empty_tuples(lst):
    return [tpl for tpl in lst if tpl]

# Example usage:
my_list = [(1, 2), (), (3, 4), (), (5, 6)]
print("List after removing empty tuples:", remove_empty_tuples(my_list))
#Python | Program to print duplicates from a list of integers:

def find_duplicates(lst):
    seen = set()
    duplicates = set(x for x in lst if x in seen or seen.add(x))
    return list(duplicates)

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 6, 4]
print("Duplicates in the list:", find_duplicates(my_list))
#Python program to find Cumulative sum of a list:
def cumulative_sum(lst):
    cum_sum = [sum(lst[:i+1]) for i in range(len(lst))]
    return cum_sum

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Cumulative sum of the list:", cumulative_sum(my_list))
#Python | Sum of number digits in List:
def sum_of_digits(lst):
    return [sum(map(int, str(num))) for num in lst]

# Example usage:
my_list = [12, 34, 56, 78]
print("Sum of digits in each number:", sum_of_digits(my_list))
#Break a list into chunks of size N in Python:
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(f"List chunks of size {chunk_size}:", chunk_list(my_list, chunk_size))
##Python | Sort the values of the first list using the second list:
def sort_using_second_list(list1, list2):
    return [value for _, value in sorted(zip(list2, list1))]

# Example usage:
list1 = [3, 1, 4, 2, 5]
list2 = ['apple', 'banana', 'orange', 'grape', 'kiwi']
sorted_list1 = sort_using_second_list(list1, list2)
print("Sorted list1 using list2:", sorted_list1)
