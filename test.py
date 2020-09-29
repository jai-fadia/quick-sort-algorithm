# import class from quick_sort.py
from quick_sort import quickSort
import numpy as np

def main():

    # create a list of random integers between -100 and 100
    myList = list(np.random.randint(-100, 100, 10))
    print(f'Unsorted list:\t\t{myList}')

    # create an object with which to sort, using the list as an input
    sorter = quickSort(myList)
    # print the sorted list
    print(f'Sorted list:\t\t{sorter.sort()}')

if __name__ == '__main__':
    main()