import asyncio
import time
async def count(a,b):
    c=a*b
    print(c)
    #await asyncio.sleep(1)
    await time.sleep(1)
    c = a + b
    print(c)

async def main():
    await asyncio.gather(count(23,32), count(12,45), count(442,212), count(442,212),count(442,212),count(442,212),count(442,212))

if __name__ == "__main__":
    #import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")



import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    #count(23, 32), count(12, 45), count(442, 212), count(442, 212), count(442, 212), count(442, 212), count(442, 212)
    for _ in range(7):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
