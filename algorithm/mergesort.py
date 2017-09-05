from tool import testtime


@testtime
def mergesort(lst):
    _helper(lst, 0, len(lst))


def _helper(lst, start, end):
    # base case
    if end - start < 2:
        return
    mid = (start + end) // 2
    _helper(lst, start, mid)
    _helper(lst, mid, end)
    _merge(lst, start, mid, end)
    return


def _merge(lst, start, mid, end):
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
    return
