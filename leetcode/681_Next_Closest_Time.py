# leetcode-weekly-contest-51
class Solution(object):

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = set()
        nums.add(int(time[0]))
        nums.add(int(time[1]))
        nums.add(int(time[3]))
        nums.add(int(time[4]))
        t = (int(time[0]), int(time[1]), int(time[3]), int(time[4]))
        from itertools import product
        mindiff = 86400
        rst = []
        for n in product(nums, repeat=4):
            if (n[0] == 2 and n[1] > 4) or n[0] > 2 or n[2] > 5 or n == t:
                continue
            tmp = self.diff(t, n)
            if tmp < mindiff:
                rst = n
                mindiff = tmp
        #print(rst)
        if not rst:
            return time
        return str(rst[0])+str(rst[1]) +':' + str(rst[2]) + str(rst[3])

    def diff(self, time1, time2):
        from datetime import timedelta
        t1 = timedelta(hours= time1[0]*10 + time1[1], minutes=time1[2]*10 + time1[3])
        t2 = timedelta(hours= time2[0]*10 + time2[1], minutes=time2[2]*10 + time2[3])
        diff = t2.total_seconds() - t1.total_seconds()
        if diff < 0:
            diff += timedelta(days=1).total_seconds()
        return diff
