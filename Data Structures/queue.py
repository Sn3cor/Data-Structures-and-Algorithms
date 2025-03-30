class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, n_val):
        newNode = Node(n_val)
        if self.head and self.tail:
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            self.head = self.tail = newNode

    def get(self):
        if not self.head or not self.tail:
            return
        if self.head == self.tail:
            val = self.head.value
            self.head = self.tail = None
            return val
        else:
            val = self.head.value
            self.head = self.head.next
            return val

def printList(head: Node):
    if not head:
        return  
    while head:
        print(f"{head.value} -> ",end="")
        head = head.next
    print("")


queue = Queue()
queue.put(10)
queue.put(11)
queue.put(123)
queue.put(15)
printList(queue.head)
queue.get()
printList(queue.head)