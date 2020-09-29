################################################################################################
###                                     Author: Jai Fadia                                    ###
### This Python file is intended to display a basic implentation of the merge sort algorithm ###
###                 Commented as thoroughly as possible to explain each step                 ###
################################################################################################

class quickSort():
    def __init__(self, myList):
        """
        Constructor function to initialize the object.

        Arguments:
        - myList: the list to be sorted
        """

        self.myList = myList

    def sort(self):
        """
        Function to use a recursive algorithm to sort a list in ascending order.

        Arguments:
        - myList: a list in any order

        Returns the list in ascending order.
        """

        # create three lists in which to store values less than, equal to, and greater than the pivot value
        less = []
        equal = []
        greater = []

        # ensure that the list is not empty - if it is, this means that all values have been sorted
        if len(self.myList) > 1:
            # assign the pivot value as the last value in the input list
            pivot = self.myList[-1]

            # calculate which values are less than, equal to, and greater than the pivot value
            less += [element for element in self.myList if element < pivot]
            equal += [element for element in self.myList if element == pivot]
            greater += [element for element in self.myList if element > pivot]
        
            # recursively continue the sorting - run the less and greater lists through the same algorithm
            return quickSort(less).sort() + equal + quickSort(greater).sort()

        # once the list is of length 0, return the final product, which is the sorted list
        return self.myList
