# 71 / 77 test cases passed.
# Status: Time Limit Exceeded
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# the test case contains very largy number (like 90w). this does not make sense
# to me. If integer 1 means one minut. one day only have 3600 minutes.
# so, the inputs (like 90w) are much bigger than my expectation.
# thats why this solution got a 'TLE'
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        last = 0
        timelot = [0]
        for interval in intervals:
            if interval.end > last:
                timelot += [0] * (interval.end-last)
                last = interval.end
            #print(timelot)
            for i in range(interval.start+1, interval.end+1):
                timelot[i] += 1
        return max(timelot)

        # 77 / 77 test cases passed.
        # Status: Accepted
        # Runtime: 68 ms
        # the while loop is like a running clock. every event (start time,
        # end time) is on the 'time line'. check every point time in order.
        # if its a event start time. check available rooms. if there is a
        #   available room, then the num of available rooms minus one. if not
        #   available room then open a new room, number of total rooms plus one.
        # if its a event end time. add one to the num of available room.
        # return the number of total rooms
        def minMeetingRooms(self, intervals):
            starts = []
            ends = []
            for interval in intervals:
                starts.append(interval.start)
                ends.append(interval.end)
            starts.sort()
            ends.sort()
            rooms = available = 0
            s = e = 0
            while s < len(intervals):
                if starts[s] < ends[e]:
                    if available > 0:
                        available -= 1
                    else:
                        rooms += 1
                    s += 1
                else:
                    available += 1
                    e += 1
            return rooms
