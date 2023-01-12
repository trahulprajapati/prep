import asyncio

def print_now(i):
    print(i)

async def keep_print(i):
    #i = 0
    while True:
        i+=1
        print_now(i)
        try:
            await asyncio.sleep(2)
        except asyncio.CancelledError:
            print('cancelled', i)
            break

async def main():
    try:
        pl1 = keep_print(1)
        pl2 = keep_print(2)
        pl3 = keep_print(3)
        #wt = asyncio.wait_for(pl, 3 )
        #await asyncio.gather(pl1, pl2, pl3) #run concurrently run inficnity
        #await asyncio.wait_for(asyncio.gather(pl1, pl2,pl3), 5) #running in timout, wait(coroutine) #giving exception GatheringFuture exception was never retrieved
        await asyncio.wait_for(asyncio.gather(pl1, pl2,pl3), 5) #so handle couting in excpetion, ti will partially canclled

        #await wt
    except Exception as e:
        print('timmme')
        #await asyncio.wait_for(keep_print(), 10)

#asyncio.run(keep_print())


asyncio.run(main())