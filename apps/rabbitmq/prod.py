from kombu import Connection, Queue, Consumer, Exchange
conn = Connection(hostname='amqp://localhost:5672/', userid='dev', password='pwd', )

cnl = conn.channel()
ex = Exchange('testex', type='direct')

q = Queue(name='testq', xchange=ex, routing_key='mytest')
# q1 = Queue(name='testq', xchange=ex, routing_key='q1')
# q2 = Queue(name='testq', xchange=ex, routing_key='q2')

def process_message(body, message):
    print('The body is {}'.format(body))
    message.ack()

#Consumer(conn, queues=q, callbacks=[process_message], accept=["text/plain"])
with Consumer(conn, queues=q, callbacks=[process_message], accept=["text/plain"]):
    #conn.drain_events(timeout=5)
   conn.drain_events()

# with Consumer(conn, queues=q1, callbacks=[process_message], accept=["text/plain"]):
#     #conn.drain_events(timeout=5)
#    conn.drain_events()
#
# with Consumer(conn, queues=q2, callbacks=[process_message], accept=["text/plain"]):
#     #conn.drain_events(timeout=5)
#    conn.drain_events()
# # class Kthlarge:
#     def __init__(self, ar):
#         self.li = ar
#
#     def left(self, i):
#         return 2 * i + 1
#
#     def right(self, i):
#         return 2 * i + 2
#
#     def left(self, i):
#         return 2 * i + 1
#
#     def has_left(self, i, n):
#         return self.left(i) < n
#
#     def has_right(self, i, n):
#         return self.right(i) < n
#
#
#     # def heapify(self, i, n):
#     #     po = i
#     #     le = self.left(i)
#     #     re = self.left(i)
#     #     if le < n and self.li[le] > self.li[po]:
#     #         po = le
#     #     if re < n and self.li[re] > self.li[po]:
#     #         po = re
#     #     if i != po:
#     #         self.li[po], self.li[i] = self.li[i], self.li[po]
#     #         self.heapify(po, n)
#
#     def heapify(self, i, n):
#          if self.has_left(i, n):
#              mi = self.left(i)
#              if self.has_right(i, n):
#                  ri = self.right(i)
#                  print(ri, '===========', self.li[mi])
#                  if self.li[ri] > self.li[mi]:
#                      mi = ri
#              print(mi)
#              if self.li[mi] > self.li[i]:
#                  self.li[mi],self.li[i] = self.li[i], self.li[mi]
#                  self.heapify(mi, n)
#     def get_largets(self):
#         print(self.li)
#         n = len(self.li)
#         self.heapify(0, n - 1)
#         print('=======')
#         print(self.li)
#
# arr=[12, 5, 787, 1, 23]
# ob = Kthlarge(arr)
# ob.get_largets()