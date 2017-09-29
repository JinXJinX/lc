import time
import random
import numpy as np
from functools import wraps

def testtime(func):
    @wraps(func)
    def wrapFunc(*args, **kwargs):
        startTime = int(round(time.time() * 1000))
        func(*args, **kwargs)
        endTime = int(round(time.time() * 1000))
        # print(endTime - startTime,'ms')
        return (endTime - startTime)
    return wrapFunc


def issorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


def randomlist(size, duplicate=False):
    return list(np.random.choice(size, size, replace=duplicate)) if size else []
