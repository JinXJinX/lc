from tool import issorted, randomlist
from mergesort import mergesort


if __name__ == '__main__':
    lst = randomlist(5000, duplicate=True)
    mergesort(lst)
    print(issorted(lst))
