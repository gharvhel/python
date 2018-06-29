def is_multiple(n, m):
    """takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    Precondition: m cannot be 0
    """
    return True if n % m == 0 else False

def main():
    print(is_multiple(10, 2))	# True
    print(is_multiple(9, 2))	# False
    print(is_multiple(10, 1))	# True
    print(is_multiple(2, 2))	# True

if __name__=='__main__':
   main()
