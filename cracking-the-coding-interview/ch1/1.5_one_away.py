"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit or zero away.

abc, ab → true
abd, abcd → true
"""
# O(n) time
# O(1) space
def one_away(string_a, string_b):
    edits = 0                 # store number of edits required
    len_a, len_b = len(string_a), len(string_b)
    index_a = index_b = 0
    if abs(len_a - len_b) > 1:  # already more that 1 edit away
        return False
    while index_a < len_a and index_b < len_b:
        ch_a, ch_b = string_a[index_a], string_b[index_b]
        if ch_a != ch_b:        # characters are not equal
            edits += 1          # increment number of edits
            if len_a == len_b:
                index_a += 1
                index_b += 1
            elif len_a > len_b:
                index_a += 1
            elif len_a < len_b:
                index_b += 1
        else:                   # characters are the same
            index_a += 1
            index_b += 1
    edits += (len_a - index_a) + (len_b - index_b)  # add remaining edits
    return True if edits < 2 else False

print(one_away('pale','ple'))
print(one_away('pales','pale'))
print(one_away('pale','bale'))
print(one_away('pale','bake'))
print(one_away('','ple'))
print(one_away('',''))
