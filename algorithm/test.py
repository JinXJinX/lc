from tool import issorted, randomlist, testtime
from mergesort import mergesort
from quicksort import quicksort
from insertionsort import insertionsort
from timsort import timsort


@testtime
def builtinsort(lst):
    lst.sort()

def testSort(func, lst1, lst2, name):
    print('--{}--'.format(name))

    # unsorted list without duplicate values
    print('list 1:')
    func(lst1)
    if not issorted(lst1):
        print('Not Sorted!!')

    # unsorted list with duplicate values
    print('list 2:')
    func(lst2)
    if not issorted(lst2):
        print('Not Sorted!!')

    # sorted list without duplicate values
    print('list 3(sorted):')
    func(lst1)
    if not issorted(lst1):
        print('Not Sorted!!')

    # sorted list with duplicate values
    print('list 4(sorted):')
    func(lst2)
    if not issorted(lst2):
        print('Not Sorted!!')


if __name__ == '__main__':
    size = 500
    lst1 = randomlist(size, duplicate=True)
    lst2 = randomlist(size, duplicate=False)

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(builtinsort, tmp1, tmp2, 'built-in sort')

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(mergesort, tmp1, tmp2, 'merge sort')

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(quicksort, tmp1, tmp2, 'quick sort')

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(insertionsort, tmp1, tmp2, 'insertion sort')

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(timsort, tmp1, tmp2, 'tim sort')
