import unittest

from tool import issorted, randomlist, testtime
from mergesort import mergesort
from quicksort import quicksort
from insertionsort import insertionsort
from timsort import timsort

@testtime
def builtinsort(lst):
    lst.sort()


class TestCase(unittest.TestCase):
    '''test func '''
    def testSort(self, func, lst1, lst2, name):
        print('--%s--' % (name))
        # unsorted list without duplicate values
        time1 = func(lst1)
        self.assertTrue(issorted(lst1))
        # unsorted list with duplicate values
        time2 = func(lst2)
        self.assertTrue(issorted(lst2))
        # sorted list without duplicate values
        time3 = func(lst1)
        self.assertTrue(issorted(lst1))
        # sorted list with duplicate values
        time4 = func(lst2)
        self.assertTrue(issorted(lst2))
        print('l1: %s ms, l2: %s ms, l1(sorted): %s ms, l2(sorted): %s ms.' % (time1, time2, time3, time4))


if __name__ == '__main__':
    size = 500
    lst1 = randomlist(size, duplicate=True)
    lst2 = randomlist(size, duplicate=False)
    lst3 = [i for i in range(size)]
    test = TestCase()

    test.testSort(builtinsort, lst1[:], lst2[:], 'built-in sort')
    test.testSort(mergesort, lst1[:], lst2[:], 'merge sort')
    test.testSort(quicksort, lst1[:], lst2[:], 'quick sort')
    test.testSort(insertionsort, lst1[:], lst2[:], 'insertion sort')
    test.testSort(timsort, lst1[:], lst2[:], 'tim sort')
