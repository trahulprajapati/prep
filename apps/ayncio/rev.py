import  asyncio


async def blckmsg(i):
    print('====',i)
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print('asd')
    print('send == ')
    await asyncio.sleep(4)
    print('end===', i)

async def run():
    f1 = blckmsg(1)
    f2 = blckmsg(2)
    f3 = blckmsg(3)
    await asyncio.gather(f1,f2,f3)
    #await asyncio.wait_for(asyncio.gather(f1,f2,f3), 30)

import time

def bl(i):
    print(i)
    time.sleep(4)

# bl(1)
# bl(2)
# bl(3)
asyncio.run(run())
