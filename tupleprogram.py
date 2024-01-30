# 1. Python program to Find the size of a Tuple
def tuple_size(t):
    return len(t)

# 2. Python – Maximum and Minimum K elements in Tuple
def max_min_k_elements(t, k):
    sorted_t = sorted(t)
    max_k_elements = sorted_t[-k:]
    min_k_elements = sorted_t[:k]
    return max_k_elements, min_k_elements

# 3. Create a list of tuples from the given list having the number and its cube in each tuple
def create_tuples_with_cube(numbers):
    tuples_with_cube = [(num, num**3) for num in numbers]
    return tuples_with_cube

# 4. Python – Adding Tuple to List and vice versa
def add_tuple_to_list(t, lst):
    return lst + list(t)

# 5. Python – Closest Pair to Kth index element in Tuple
def closest_pair_to_kth_index(t, k):
    t_sorted = sorted(t, key=lambda x: abs(x - k))
    return t_sorted[:2]

# 6. Python – Join Tuples if similar initial element
def join_similar_initial_element(tuples):
    result = []
    tuples_dict = {}
    for tup in tuples:
        key = tup[0]
        if key in tuples_dict:
            tuples_dict[key] += tup[1:]
        else:
            tuples_dict[key] = tup
    result = list(tuples_dict.values())
    return result

# 7. Python – Extract digits from Tuple list
def extract_digits_from_tuples(tuples_list):
    digits = [digit for tup in tuples_list for digit in str(tup[1])]
    return digits

# 8. Python – All pair combinations of 2 tuples
def all_pair_combinations(t1, t2):
    pairs = [(x, y) for x in t1 for y in t2]
    return pairs

# 9. Python – Remove Tuples of Length K
def remove_tuples_of_length_k(tuples_list, k):
    result = [tup for tup in tuples_list if len(tup) != k]
    return result

# 10. Sort a list of tuples by the second Item
def sort_tuples_by_second_item(tuples_list):
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    return sorted_tuples

# 11. Python program to Order Tuples using external List
def order_tuples_using_external_list(tuples_list, order_list):
    ordered_tuples = [tuples_list[i] for i in order_list]
    return ordered_tuples

# 12. Python – Flatten tuple of List to tuple
def flatten_tuple_of_list(tuple_of_list):
    flattened_tuple = tuple(item for sublist in tuple_of_list for item in sublist)
    return flattened_tuple

# 13. Python – Convert Nested Tuple to Custom Key Dictionary
def nested_tuple_to_dict(nested_tuple):
    result_dict = {}
    for tup in nested_tuple:
        key = tup[0]
        if key not in result_dict:
            result_dict[key] = []
        result_dict[key].append(tup[1:])
    return result_dict
 