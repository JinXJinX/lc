# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 36 ms
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, v in enumerate(numbers):
            if v in dic:
                index1 = dic[v]
                if index1 < i:
                    index1, i = i, index1
                return [i+1, index1+1]
            else:
                dic[target-v] = i
        return None


# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# since the given list is sorted, two pointers might be the better answer.
class Solution(object):
    def twoSum(self, numbers, target):
        l, h = 0, len(numbers) -1
        while l < h:
            s = numbers[l] + numbers[h]
            if s == target:
                return [l+1, h+1]
            elif s < target:
                l += 1
            else:
                h -= 1
        return None
