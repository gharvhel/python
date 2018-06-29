def is_distinct(seq):
    """takes a sequence of numbers and determines
    if all the numbers are different from each other"""
    seq_set = set()
    distinct = True
    for i in seq:
        if i in seq_set:
            distinct = False
            break
        else:
            seq_set.add(i)
    return distinct

def main():
    print(is_distinct([1,2,3,4]))
    print(is_distinct([1,1]))
    print(is_distinct([1,23,2,3]))

if __name__=='__main__':
   main()
