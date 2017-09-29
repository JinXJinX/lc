from tool import testtime, randomlist, issorted
from collections import Counter
'''
time complexity: Ω(1); Θ(1); O(1)
space complexity: O(n)
'''
@testtime
def countingsort(lst):
    counting = Counter(lst)
    idx = 0
    for i, num in sorted(counting.items()):
        for _ in range(num):
            lst[idx] = i
            idx += 1


if __name__ == '__main__':
    size = 20
    lst = randomlist(size, duplicate=True)
    countingsort(lst)
    print(lst)
    print(issorted(lst))
