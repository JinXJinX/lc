def test(lst, k):
    return sorted(lst)[k-1]

if __name__ == '__main__':
    print(test([5,3,2,1,2,3,4,5,2],4))
