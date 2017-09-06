from tool import testtime, randomlist, issorted

'''
time complexity: Ω(nlogn); Θ(nlogn); O(n^2)
space complexity: O(logn)
'''
# TODO, update algorithm for handle sorted list
@testtime
def quicksort(lst):
    _helper(lst, 0, len(lst))


def _helper(lst, lo, hi):
    if lo < hi:
        try:
            p = partition(lst, lo, hi)
        except RuntimeError:
            print('error', lo, hi)
            return
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
    size = 500
    lst = randomlist(size, duplicate=True)
    quicksort(lst)
    print(issorted(lst))
