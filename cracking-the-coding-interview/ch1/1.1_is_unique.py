"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures
"""
ASCII_LEN = 128
# O(n) time : for loop on chrs
# O(n) space: set
def is_unique1(string):
    if len(string) < 2:            # Trivial Cases
        return True
    elif len(string) > ASCII_LEN:
        return False
    chr_set = set()
    for c in string:
        if c in chr_set:
            return False
        else:
            chr_set.add(c)
    return True

# O(nlogn) time : sort
# O(n) space
def is_unique2(string):
    if len(string) < 2:            # Trivial Cases
        return True
    elif len(string) > ASCII_LEN:
        return False
    string = sorted(string)
    for c in range(len(string) - 1):
        if string[c] == string[c+1]:
            return False
    return True

# O(n) time
# O(1) space
def is_unique(string):
    if len(string) < 2:            # Trivial Cases
        return True
    elif len(string) > ASCII_LEN:
        return False
    bool_arr = [False] * ASCII_LEN    # For unicode chars/ 256 for extended
    for c in string:
        if bool_arr[ord(c)] == True:    # Character already exist
            return False
        else:
            bool_arr[ord(c)]  = True    # Character seen for the first time
    return True

print(is_unique1(""))
print(is_unique1("a"))
print(is_unique1("abc"))
print(is_unique1("abac"))
print('----------')
print(is_unique2(""))
print(is_unique2("a"))
print(is_unique2("abc"))
print(is_unique2("abac"))
print('----------')
print(is_unique(""))
print(is_unique("a"))
print(is_unique("abc"))
print(is_unique("abac"))
print('----------')
