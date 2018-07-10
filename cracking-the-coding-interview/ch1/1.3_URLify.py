"""
Write a method to replace all spaces in a string with %20.
You and given the true length of the string n

"""
def count_spaces(char_arr, n):
    count = 0
    for c in char_arr[:n]:
        if c == ' ':
            count += 1
    return count


def URLify(char_arr, true_length):
    spaces = count_spaces(char_arr, true_length)
    index = true_length - 1 + spaces * 2
    for i in range(true_length-1, -1, -1):
        ch = char_arr[i]
        if ch == ' ':
            char_arr[index] = '0'
            char_arr[index - 1] = '2'
            char_arr[index - 2] = '%'
            index -= 3
        else:
            char_arr[index] = ch
            index -= 1
arr = ['a',' ','b',' ','c',' ',' ',' ',' ']
URLify(arr, 5)
print(''.join(arr))
