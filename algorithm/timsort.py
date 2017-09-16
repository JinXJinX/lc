from tool import testtime, randomlist, issorted

'''
time complexity: Ω(n); Θ(nlogn); O(nlogn)
space complexity: O(n)
TODO: sorting unsorted list, takes too long. minrun should be
      changed according to the list size
'''
@testtime
def timsort(lst):
    if len(lst) < 64:
        minrun = len(lst)
    else:
        minrun = int(bin(len(lst))[2:8], 2)
    helper(lst, 0, len(lst)//2, len(lst), minrun)


def helper(lst, start, mid, end, minrun):
    if end - start < minrun:
        insertionsort(lst)
        return
    helper(lst, start, (start+mid)//2, mid, minrun)
    helper(lst, mid, (mid+end)//2, end, minrun)
    merge(lst, start, mid, end)


def insertionsort(lst):
    for i in range(1, len(lst)):
        tmp = i
        while tmp > 0 and lst[tmp-1] > lst[tmp]:
            lst[tmp-1], lst[tmp] = lst[tmp], lst[tmp-1]
            tmp -= 1


def merge(lst, start, mid, end):
    left_idx = start
    right_idx = mid
    tmp = []
    for i in range(end - start):
        if lst[left_idx] < lst[right_idx]:
            tmp.append(lst[left_idx])
            left_idx += 1
        else:
            tmp.append(lst[right_idx])
            right_idx += 1
        if left_idx >= mid:
            tmp += lst[right_idx:end]
            break
        elif right_idx >= end:
            tmp += lst[left_idx:mid]
            break
    lst[start:end] = tmp[:]


if __name__ == '__main__':
    size = 2000
    lst = randomlist(size, duplicate=True)
    timsort(lst)
    print(issorted(lst))
