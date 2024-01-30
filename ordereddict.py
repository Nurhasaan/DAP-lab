from collections import OrderedDict, Counter

# 18. Check if binary representations of two numbers are anagram
def are_binary_anagrams(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]
    return Counter(bin_num1) == Counter(bin_num2)

# 19. Python Counter to find the size of the largest subset of anagram words
def largest_anagram_subset(words):
    anagram_counts = Counter([''.join(sorted(word)) for word in words])
    return max(anagram_counts.values(), default=0)

# 20. Python | Remove all duplicate words from a given sentence
def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = list(OrderedDict.fromkeys(words))
    return ' '.join(unique_words)

# 21. Python Dictionary to find mirror characters in a string
def find_mirror_characters(s):
    mirror_dict = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b'}
    mirrored_chars = [mirror_dict.get(char, char) for char in s]
    return ''.join(mirrored_chars)

# 22. Counting the frequencies in a list using dictionary in Python
def count_frequencies(lst):
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

# 23. Python | Convert a list of Tuples into a Dictionary
def tuples_to_dict(tuples_list):
    return dict(tuples_list)

# 24. Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
def can_make_string(source, target):
    source_counter = Counter(source)
    target_counter = Counter(target)
    intersection = source_counter & target_counter
    return len(target) == sum(intersection.values())

# 25. Python dictionary, set, and counter to check if frequencies can become the same
def can_frequencies_become_same(lst):
    freq_counter = Counter(lst)
    values_set = set(freq_counter.values())
    return len(values_set) == 1 or (len(values_set) == 2 and 1 in values_set)

# 26. Scraping And Finding Ordered Words In A Dictionary using Python
# (Implementation depends on the available dictionary or source of words)

# 27. Possible Words using given characters in Python
def possible_words(characters, dictionary):
    possible_words_list = [word for word in dictionary if set(word).issubset(set(characters))]
    return possible_words_list

# 28. Python – Keys associated with Values in Dictionary
def keys_associated_with_values(dictionary, target_values):
    associated_keys = [key for key, value in dictionary.items() if value in target_values]
    return associated_keys
