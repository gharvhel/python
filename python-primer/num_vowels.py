def num_vowels():
    """counts the number of vowels in a given
    character string"""
    print(sum([1 for c in input('Enter a sentence:') if c in {*'aeiouAEIOU'}]))

def main():
    num_vowels()

if __name__=='__main__':
    main()
