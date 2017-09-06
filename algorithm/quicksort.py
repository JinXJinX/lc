from tool import testtime, randomlist, issorted

'''
time complexity: Ω(nlogn); Θ(nlogn); O(n^2)
space complexity: O(1)

quicksort performs bad when every pivot is the max/min in current range.

In this implementation, a sorted list will spend a O(n^2) running time,
if the size of sorted list is greater than 1000, this algorithm is easy to
reach the maximum recursion depth exceeded in comparison. use iteration indeed
of recursion, might aviod this run time error.

"RuntimeError: maximum recursion depth exceeded in comparison" is a guard
against a stack overflow. could use sys.getrecursionlimit() to increase
limitation.
'''
@testtime
def quicksort(lst):
    # handle maximum recursion depth exceeded error
    try:
        _helper(lst, 0, len(lst))
    except RuntimeError as err:
        print(err)


def _helper(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        _helper(lst, lo, p)
        _helper(lst, p+1, hi)
    return


def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi-1] <= lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
    return i+1


if __name__ == '__main__':
    size = 2000
    lst = randomlist(size, duplicate=True)
    quicksort(lst)
    print(issorted(lst))
