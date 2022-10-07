def it():
    li = {1:'a', 2: 'b', 3: 'c'}
    l2 = ['k1', 'k2']
    #di =  {
    #     'k1' : {1:'a', 2: 'b', 3: 'c'},
    #     'k2' :{1:'a', 2: 'b', 3: 'c'}
    # }
    di = {}

    for i in l2:
        di[i] = li
    return  di

def gen():
    li = {1:'a', 2: 'b', 3: 'c'}
    l2 = ['k1', 'k2']
    #di =  {
    #     'k1' : {1:'a', 2: 'b', 3: 'c'},
    #     'k2' :{1:'a', 2: 'b', 3: 'c'}
    # }
    #di = {}

    for i in l2:
        di = {}
        di['name'] = i
        di['value'] = li
        yield di
        #di[i] = li
    #return  di

#iter
print(it())

#generator
g = gen()
cdict = {c['name']:c['value'] for c in g}
va  =cdict['k1'].pop(1)
print(va)
#d
#print(gen())
print((cdict))