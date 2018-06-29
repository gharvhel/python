from random import randrange

def choice(seq):
    """Using only randrange, implements function similar to python's
    random choice() function"""
    random_index = randrange(0,len(seq))
    return seq[random_index]

def main():
    print(choice([1,2,3,4,5]))
    print(choice([1,2,3,4,5]))
    print(choice([1,2,3,4,5]))
    print(choice([1,2,3,4,5]))
    print(choice([1,2,3,4,5]))
    print(choice([1,2,3,4,5]))

if __name__=='__main__':
    main()
