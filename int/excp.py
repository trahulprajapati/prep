
def t1():
    try:
       t2()
    except Exception as e:
        print('in t1')
    t2()
    print('exe nooo')


def t2():
    try:
        t3()
    except Exception as e:
        raise Exception('t1 no')
        print('in t2', e)


def t3():
    raise Exception('nooo')

#import http.client
import requests
try:
    x = requests.get('http://localhost:8001/api/v1/transactions/')
except Exception as e:
    print(e)
#http://localhost:13110/api/v1/transactions/
#print(x)
#t1()