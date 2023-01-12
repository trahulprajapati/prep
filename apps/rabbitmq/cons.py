from kombu import Connection, Queue, Producer, Exchange
import time
rabbit_url = "amqp://localhost:5672/"
#conn = Connection(rabbit_url)
conn = Connection(hostname='amqp://localhost:5672/', userid='dev', password='pwd', )

cnl = conn.channel()
ex = Exchange('testex', type='direct')
pr = Producer(channel=cnl, exchange=ex, routing_key='mytest')

q = Queue(name='testq', exchange=ex, routing_key='mytest', channel=cnl)
q.maybe_bind(conn)

q.declare()

while True:
    pr.publish('Hello from learning!')
    time.sleep(5)