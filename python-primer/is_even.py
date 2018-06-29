def is_even(k):
    """ takes an integer value and returns True if k is even, 
    and False otherwise.
    function cannot use the multiplication, modulo, or division operators."""
    return True if k & 0b1 == 0 else False

def main():
    print(is_even(0))		# True
    print(is_even(-1))		# False
    print(is_even(1))		# False
    print(is_even(2))		# True
    print(is_even(134567))	# False
    print(is_even(134568))	# True

if __name__=='__main__':
    main()
