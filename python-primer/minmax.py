def minmax(seq):
    """takes a sequence of one or more numbers, 
    and returns the smallest and largest numbers, 
    in the form of a tuple of length two."""
    min_num = max_num = seq[0]
    for i in range(1, len(seq)):
        min_num = seq[i] if min_num > seq[i] else min_num 
        max_num = seq[i] if max_num < seq[i] else max_num
    return (min_num, max_num)

def main():
    print(minmax([1,2,3,4]))
    print(minmax([1,]))
    print(minmax([23,-2,3,4,6,72,3]))
    print(minmax([0,0,0,0]))
    print(minmax([12]))
 
if __name__=="__main__":
    main()
