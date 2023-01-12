import asyncio

# this is callback


def callbacks1(fu):
    fi = fu.result()
    print("in scond call", fu, fi)


def callback2(fu):
    fi = fu.result()
    print("in scond call", fu, fi)


# get result
async def get_result(aw):
    return await aw


loop = asyncio.get_event_loop()
f = asyncio.Future()

# registering callback to future - done calback

f.add_done_callback(
    callbacks1
)  # first calback when future getrsult or excpetion then this will be called
f.add_done_callback(callback2)  # second calback
f.add_done_callback(lambda f: loop.stop())
f.set_result([1, 2])
# f.set_exception(ValueError('second : '))
loop.run_forever()

print(asyncio.__file__)

# result-
# loop.call_later(5, f.set_result, 'param1')
# #loop.run_forever(asyncio.gather(get_result(f), get_result(f),get_result(f)))
# loop.run_until_complete(asyncio.gather(get_result(f), get_result(f),get_result(f)))


def tmp():
    for i in range(4):
        yield i


t = tmp()
t.send(123)
print(t.gi_running)
