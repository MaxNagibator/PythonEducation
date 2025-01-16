import asyncio
import time
from asyncio import tasks
from time import sleep


class Test(object):
    _i = 0

    @property
    def i(self):
        return type(self)._i

    @i.setter
    def i(self, value):
        self._i = value


x33 = Test()

async def fun1(n, delay):
    print(time.strftime('%X'), n)
    await asyncio.sleep(delay)
    print(time.strftime('%X'), 'fun1 завершена',n)

async def worker(tasks, results):
    # individual worker task (sometimes called consumer)
    # - sequentially process tasks as they come into the queue
    # and emit the results
    while True:
        n, d = await tasks.get()
        result = await fun1(n, d)
        await results.put(result)

async def assigner(tasks):
    # come up with tasks dynamically and enqueue them for processing
    task_n = 0
    while True:
        # await asyncio.sleep(1)
        task_n += 1
        await tasks.put((task_n, 2))

async def displayer(q):
    # show results of the tasks as they arrive
    while True:
        result = await q.get()
        print(result)

async def main(pool_size):
    tasks = asyncio.Queue(10)
    results = asyncio.Queue(10)
    workers = [asyncio.create_task(worker(tasks, results))
                for _ in range(pool_size)]
    await asyncio.gather(assigner(tasks), displayer(results), *workers)

   #for i in range(1, 10):
   #    tasks.append(asyncio.create_task(fun1(i)))

   # for task in tasks:
   #     await task

   #await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
   #await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)


print(time.strftime('%X'))
asyncio.run(main(5))
print(time.strftime('%X'))
