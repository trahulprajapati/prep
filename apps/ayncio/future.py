import asyncio

async def get_res(aw):
    try:
        res = await aw
    except Exception as e:
        print('sometinhg wrong ', e)
        return 'noooo res'
    else:
        return res

f = asyncio.Future()
loop = asyncio.get_event_loop()
#
# #f.set_result('Hiii this is resulty')
# loop.call_later(5, f.set_result, 'thiisii')
# #loop.call_later(5, f.set_result)
#
# pl = loop.run_until_complete(get_res(f))
# print(pl)


#wrapp
# f = asyncio.Future()
# loop.call_later(15, f.set_result, 'thiisii')
# pl = loop.run_until_complete(get_res(get_res(get_res(f))))
# print(pl)

#set expecetion
# f = asyncio.Future()
# loop.call_later(10, f.set_exception, ValueError('Errrororro '))
# pl = loop.run_until_complete(get_res(f))
# print(pl)

#cancel
# f = asyncio.Future()
# loop.call_later(10, f.cancel)
# pl = loop.run_until_complete(get_res(f))
# print(pl)

#multple coroutine
f = asyncio.Future()
loop.call_later(10, f.set_result, 'ths is res')
pl = loop.run_until_complete(asyncio.gather(get_res(f), get_res(f),get_res(f)) )
print(pl)