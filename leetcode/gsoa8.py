def test(lst, target):
    from collections import defaultdict
    dic = defaultdict(int)
    for num in lst:
        key = target - num
        dic[key] += 1
    rst = 0
    for num in set(lst):
        key = target - num
        if key == num:
            rst += dic[num] * (dic[num]-1) * 0.5
        else:
            rst += dic[num] * dic[key]
        del dic[num]
    return int(rst)

if __name__ == '__main__':
    lst = [1,5,3,2,1,2,0,3]
    print(test(lst,5))

    lst = [1,1,1,3]
    print(test(lst,2))
