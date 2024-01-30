# 1. Python – Extract Unique values dictionary values
def unique_values(dictionary):
    unique_values_set = set(value for values in dictionary.values() for value in values)
    return list(unique_values_set)

# 2. Python program to find the sum of all items in a dictionary
def sum_of_items(dictionary):
    return sum(dictionary.values())

# 3. Python | Ways to remove a key from dictionary
def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]

# 4. Ways to sort a list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter
def sort_dict_by_values_itemgetter(dictionary):
    return sorted(dictionary.items(), key=itemgetter(1))

# 5. Ways to sort a list of dictionaries by values in Python – Using lambda function
def sort_dict_by_values_lambda(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1])

# 6. Python | Merging two Dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# 7. Python – Convert key-values list to a flat dictionary
def flatten_dictionary(key_values_list):
    flat_dict = {key: value for keys_values in key_values_list for key, value in keys_values.items()}
    return flat_dict

# 8. Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict
def insert_at_beginning_ordered_dict(ordered_dict, key, value):
    ordered_dict[key] = value
    return OrderedDict([(key, value)] + list(ordered_dict.items()))

# 9. Python | Check order of character in string using OrderedDict( )
def check_order_of_characters(s, order):
    char_index = OrderedDict.fromkeys(order)
    return set(char_index) == set(s)

# 10. Dictionary and counter in Python to find the winner of the election
from collections import Counter
def election_winner(votes):
    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]
    return winners

# 11. Python – Append Dictionary Keys and Values (In order) in a dictionary
def append_dict_keys_values(dictionary):
    result_dict = {}
    for key, value in dictionary.items():
        result_dict[key] = value
        result_dict[value] = key
    return result_dict

# 12. Python | Sort Python Dictionaries by Key or Value
def sort_dictionary(dictionary, by_key=True):
    return dict(sorted(dictionary.items(), key=lambda x: x[0 if by_key else 1]))

# 13. Python – Sort Dictionary key and values List
def sort_dict_keys_values_list(dictionary):
    sorted_keys_values = sorted(dictionary.items())
    sorted_keys = [key for key, _ in sorted_keys_values]
    sorted_values = [value for _, value in sorted_keys_values]
    return sorted_keys, sorted_values

# 14. Handling missing keys in Python dictionaries
def get_value_with_default(dictionary, key, default_value):
    return dictionary.get(key, default_value)

# 15. Python dictionary with keys having multiple inputs
def create_dictionary_with_multiple_inputs(keys, values):
    return dict(zip(keys, values))

# 16. Print anagrams together in Python using List and Dictionary
def group_anagrams(words):
    anagrams_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    return list(anagrams_dict.values())

# 17. K’th Non-repeating Character in Python using List Comprehension
def kth_non_repeating_character(s, k):
    char_counts = Counter(s)
    non_repeating_chars = [char for char, count in char_counts.items() if count == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    else:
        return None
