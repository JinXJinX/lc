# 111 / 111 test cases passed.
# Status: Accepted
# Runtime: 95 ms

# a better solution could use the given point, to serach all black pixle
# and get the four corners
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum('1' in r for r in image) * sum('1' in r for r in zip(*image))
