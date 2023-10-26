
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()  # declare constructor using class stack
print(s.isEmpty())  # true
s.push(4)  # [4]
s.push('dog')  # [4,'dog']
print(s.peek())  # 'dog'
s.push(True)  # [4,'dog',True]
print(s.size())  # [3]
print(s.isEmpty())  # false
s.push(8.4)  # [4,'dog',True,8.4]
print(s.pop())  # [4,'dog',True] = print 8.4 then delete
print(s.pop())  # [4,'dog'] = print True then delete
print(s.size())  # [2]