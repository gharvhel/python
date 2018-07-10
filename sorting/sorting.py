import time
import random

def insertion_sort(seq):
    """
    [5,3,6,1]
    k = 1
    j = 1
    current = 3
    seq[j] = 3
    seq[j-1] = 5
    """
    for k in range(1, len(seq)):
        current = seq[k]
        j = k
        while j > 0 and current < seq[j-1]:
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = current

if __name__=='__main__':
    # Create a random list of intergers
    unsorted = [random.randint(0,101) for _ in range(10)]
    print('Unsorted:', unsorted)

    # Sort the list and time it
    start_time = time.time()
    insertion_sort(unsorted)
    end_time = time.time()

    print('Sorted:', unsorted)

    total_time = start_time - end_time
    print('The total time:', total_time)
