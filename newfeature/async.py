import types

async def coro1():
    print("C1: Start")
    await switch()
    print("C1: Stop")

async def coro2():
    print("C2: Start")
    print("C2: a")
    print("C2: b")
    print("C2: c")
    print("C2: Stop")

@types.coroutine
def switch():
    yield


def run(coros):
    co1 = coros[:]

    while co1:
        # Duplicate list for iteration so we can remove from original list.
        tmp = co1[:]
        for coro in tmp:
            try:
                coro.send(None)
            except StopIteration:
                co1.remove(coro)

c1 = coro1()
c2 = coro2()
run([c1, c2])
