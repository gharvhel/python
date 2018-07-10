
"""
Given a string, write a function to check if it is a permutation of a palindrome.
"""
def is_palindrome_permutation(string):
    letters = [0] * 128     # Ascii assumption
    for ch in string:
        if ch == ' ':
            continue
        if letters[ord(ch)] == 0:
            letters[ord(ch)]     = 1
        elif letters[ord(ch)] == 1:
            letters[ord(ch)]     = 0
    odds_count = letters.count(1)
    return True if odds_count < 2 else False

print(is_palindrome_permutation("taco cat"))
print(is_palindrome_permutation("tact coa"))
print(is_palindrome_permutation("a"))
print(is_palindrome_permutation(""))
print(is_palindrome_permutation("ab"))
