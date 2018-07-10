"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
ASCII_LEN = 128
def is_permutation(string_a, string_b):
    if 0 == len(string_a) == len(string_b):        #Trivial cases
        return True
    elif len(string_a) != len(string_b):
        return False
    char_count = [0] * ASCII_LEN        # Dictionary to count characters
    for i in range(len(string_a)):
        ch_a = string_a[i]
        ch_b = string_b[i]
        char_count[ord(ch_a)] += 1
        char_count[ord(ch_b)] -= 1

    for i in char_count:
        if i != 0:
            return False
    return True


print(is_permutation("", ""))
print(is_permutation("a", ""))
print(is_permutation("a", "a"))
print(is_permutation("abc", "cba"))
print(is_permutation("aaartt", "taraat"))
