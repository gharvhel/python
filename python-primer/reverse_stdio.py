from sys import stdin

def reverse_stdio():
    lines = [line for line in stdin]
    for line in lines[::-1]:
        print(line, end='')

def main():
    reverse_stdio()

if __name__=="__main__":
    main()
