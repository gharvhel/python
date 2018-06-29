def odd_pair(seq):
    """ takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd"""
    found = False
    for i, x in enumerate(seq):    
        for j, y in enumerate(seq):
            if i == j or x == y:
                continue
            else:
                 if is_odd(x * y):
                     found = True
    return found

def is_odd(num):
    return True if num % 2 == 1 else False    

def main():
    print(odd_pair([1,1,1,1]))
    print(odd_pair([1,2,3]))
    print(odd_pair([0,2,4,6]))
    print(odd_pair([1,3,5,7]))
    print(odd_pair([1,1]))
    print(odd_pair([-1,-5,-6]))

if __name__=='__main__':
    main()

