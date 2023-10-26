from Queue import Queue
from Stack import Stack

s = Stack()  # ประกาศ constructor เรียกใช้ class stack
print(s.isEmpty())  # true
s.push(4)  # [4]
s.push('dog')  # [4,'dog']
print(s.peek())  # 'dog'
s.push(True)  # [4,'dog',True]
print(s.size())  # [3]
print(s.isEmpty())  # false
s.push(8.4)  # [4,'dog',True,8.4]
print(s.pop())  # [4,'dog',True] = print 8.4 แล้วลบ
print(s.pop())  # [4,'dog'] = print True แล้วลบ
print(s.size())  # [2]

print('---------------------------------------------------------')

q = Queue()  # ประกาศ constructor เรียกใช้ class stack
q.enqueue('dog')# ['dog']
q.enqueue(4)
q.enqueue(True)
print('Queue size:', q.size())
b = q.dequeue()
print('Result of dequeue', b)
print('Queue size:', q.size())
