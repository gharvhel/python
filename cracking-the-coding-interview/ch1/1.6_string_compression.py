"""
Implement a method to perform basic string compression using the counts of repeated characters.

aabcccccaaa → a2b1c5a3
"""
def string_compression(string):
    if len(string) < 1:        # trivial cases
        return string
    chr_list = []
    current = string[0]
    count = 0
    for c in string:
        if current == c:
            count += 1
        else:
            chr_list.extend([current, str(count)])
            count = 1
            current = c
    chr_list.extend([current, str(count)])
    # print(len(chr_list) , len(string))
    return ''.join(chr_list) if len(chr_list) <= len(string) else string

while True:
    string = str(input("Enter a phrase:"))
    print(f"Compressed: {string_compression(string)}")
