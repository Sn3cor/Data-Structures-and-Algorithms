class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Stack():
    def __init__(self):
        self.top = Node(None)
    
    def push(self,n_val):
        newNode = Node(n_val)
        newNode.next = self.top.next
        self.top.next = newNode

    
    def pop(self):
        self.top.next = self.top.next.next
        #return self.top

def printList(head: Node):
    if not head:
        return
    head = head.next
    while head:
        print(f"{head.value} -> ",end="")
        head = head.next
    print("")

stack = Stack()
stack.push(10)
stack.push(12)
stack.push(122)
printList(stack.top)
stack.pop()
printList(stack.top)
