def sum_square(n):
    """Takes a positive integer n and returns the sum of 
    the squares of all the positive integers smaller than n."""
    sum = 0
    for i in range(n):
        sum += i * i
    return sum

def main():
    print(sum_square(1))
    print(sum_square(2))
    print(sum_square(5))
    print(sum_square(8))
    print(sum_square(10))
    print(sum_square(15))

if __name__=="__main__":
    main()
