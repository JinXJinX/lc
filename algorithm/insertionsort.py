from tool import testtime, randomlist, issorted

'''
time complexity: Ω(n); Θ(n^2); O(n^2)
space complexity: O(1)
insertion sort works very well wtih sorted list,
how every, the it takes n^2 time, for unsorted list.
'''
@testtime
def insertionsort(lst):
    for i in range(1, len(lst)):
        tmp = i
        while tmp > 0 and lst[tmp-1] > lst[tmp]:
            lst[tmp-1], lst[tmp] = lst[tmp], lst[tmp-1]
            tmp -= 1
    return


if __name__ == '__main__':
    size = 2000
    lst = randomlist(size, duplicate=True)
    insertionsort(lst)
    print(issorted(lst))
