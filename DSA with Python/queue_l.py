from winreg import REG_OPTION_NON_VOLATILE


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
 
a_queue = Queue()
while True:
    print('1.Enqueue')
    print('2.dequeue')
    print('3.quit')
    print('What would you like to do? ')
    do = input().split()
 
    operation = do[0].strip().lower()
    if operation == '1':
        print("Enqueue Value : ")
        a_queue.enqueue(int(do[1]))
    elif operation == '2':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == '3':
        break
    else:
        print("Invalid Choice..!")