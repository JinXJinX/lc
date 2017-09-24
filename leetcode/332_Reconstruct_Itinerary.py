# 80 / 80 test cases passed.
# Status: Accepted
# Runtime: 95 ms
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # targets = collections.defaultdict(list)
        # for fr, to in sorted(tickets, reverse=True):
        #     targets[fr] += to,
        # route = []
        # print(targets)
        # def visit(airport):
        #     while targets[airport]:
        #         visit(targets[airport].pop())
        #     route.append(airport)
        # visit('JFK')
        # return route[::-1]
        targets = {}
        for fr, to in sorted(tickets, reverse=True):
            targets[fr] = targets.get(fr, []) + [to]
        route = []
        #print(targets)
        def visit(airport):
            while airport in targets and targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
