class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def createList(values: list[int]):
        foo = Node()
        ptr = foo
        for value in values:
            ptr.next = Node(value)
            ptr = ptr.next
        return foo.next
    
def printList(head: Node):
    if not head:
        return
    while head:
        print(f"{head.value} -> ",end="")
        head = head.next
    print("")
#######################################################################
# 
#   MERGE SORT
#
#######################################################################
def merge(list1:Node,list2:Node):
    foo = Node()
    ptr = foo

    while list1 and list2:
        if list1.value>list2.value:
            ptr.next = list2
            ptr = ptr.next
            list2 = list2.next
        else:
            ptr.next = list1
            ptr = ptr.next
            list1 = list1.next

    if list1:
        ptr.next = list1
    if list2:
        ptr.next = list2

    return foo.next

def mergeSort(list):
    n=0
    ptr = list
    while ptr:
        n+=1
        ptr=ptr.next
    
    def find_mid(list,n):
        mid = (n//2) - 1 
        ptr_mid=list
        i=0
        while i<mid:
            ptr_mid = ptr_mid.next
            i+=1
        prev_mid = ptr_mid
        ptr_mid = ptr_mid.next
        prev_mid.next = None
        return ptr_mid
    
    def sorting(list,n):
        if not list.next:
            return list
        if list.next:
            mid = find_mid(list,n)
            
            list = sorting(list,n//2)
            mid = sorting(mid, n-(n//2))
            return merge(list,mid)
        
    return sorting(list, n)


list1 = Node.createList([1,5,7,9,11])
list2 = Node.createList([2,4,5,6,8,10,12,14,51])
printList(list1)
list = merge(list1, list2)
printList(list)

test = Node.createList([5,12,4,11,17,19,20])
test = mergeSort(test)
printList(test)
