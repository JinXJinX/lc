# 481 / 481 test cases passed.
# Status: Accepted
# Runtime: 192 ms

class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O','U']
        lst = list(s)
        l, r = 0, len(lst) - 1

        while r > l:
            while r > l:
                if lst[l] in vowels:
                    break
                else:
                    l += 1
            while r > l:
                if lst[r] in vowels:
                    break
                else:
                    r -= 1
            lst[l], lst[r] = lst[r], lst[l]
            r -= 1
            l += 1
        return ''.join(lst)
