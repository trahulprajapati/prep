import asyncio

async def f1(f):
    while True:
        print(f)
        await asyncio.sleep(2)
    # for i in range(5, -1, -1):
    #     print('before', f)
    #     await asyncio.sleep(i)
    #     print('after', f)
    # print('in f1 before')
    # await asyncio.sleep(15)
    # print('in f1 after, starting second')
    # await asyncio.sleep(15)
    # print('finish second')


async def f2():
    print('in f2 before')
    await asyncio.sleep(15)
    print('in f2 after')


async def main():
    await asyncio.wait_for(asyncio.gather(f1('fi'),f1('f2'),f1('f3')), 10)
    #await asyncio.gather(f1('fi'),f1('f2'),f1('f3'))
    #await asyncio.gather(f1(), f2(), f1())


#await main()
asyncio.run(main())


