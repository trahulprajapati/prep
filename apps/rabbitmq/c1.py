from kombu import Connection, Queue, Consumer, Exchange
conn = Connection(hostname='amqp://localhost:5672/', userid='dev', password='pwd', )

cnl = conn.channel()
ex = Exchange('testex', type='direct')


q1 = Queue(name='testq', xchange=ex, routing_key='q1')


def process_message(body, message):
    print('The body is {}'.format(body))
    message.ack()


while True:
    with Consumer(conn, queues=q1, callbacks=[process_message], accept=["text/plain"]):
        #conn.drain_events(timeout=5)
       conn.drain_events()

