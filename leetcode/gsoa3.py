def test(n):
    if n <= 3:
        return n
    res = [0] * n
    res[0], res[1], res[2] = 1, 2, 3
    for i in range(3, n):
        res[i] = res[i-1] + res[i-2]+ res[i-3]
    # print(res)
    return res[-1]

if __name__ == '__main__':
    print(test(5))
