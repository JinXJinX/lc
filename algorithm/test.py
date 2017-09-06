from tool import issorted, randomlist
from mergesort import mergesort
from quicksort import quicksort


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

    print('----')


if __name__ == '__main__':
    size = 5000
    lst1 = randomlist(size, duplicate=True)
    lst2 = randomlist(size, duplicate=False)

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(mergesort, tmp1, tmp2, 'merge sort')

    tmp1 = lst1[:]
    tmp2 = lst2[:]
    testSort(quicksort, tmp1, tmp2, 'quick sort')
