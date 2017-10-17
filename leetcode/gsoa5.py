        from collections import Counter
        c = Counter(s)
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        return -1
