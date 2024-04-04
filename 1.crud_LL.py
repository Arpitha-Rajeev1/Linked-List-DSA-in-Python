class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#this has time complexity of n^2
def create():
    inputList = [int(i) for i in input().split()]
    head = None
    for currData in inputList:
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            data = head
            while data.next is not None:
                data = data.next
            data.next = newNode
    return head

#this has time complexity of n
def createOpt():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def read(head):
    while head is not None:
        print(head.data, '-> ', end = '')
        head = head.next
    print('None')

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

#inserting at i
def update(head, i, ele):
    
    if i < 0 or i > length(head):
        return head
    
    count = 0
    prev = None
    curr = head
    
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
        
    newNode = Node(ele)
    
    if prev is None:
        head = newNode
    else:
        prev.next = newNode
    newNode.next = curr

    return head

#using recursion
def updateR(head, i, data):
    if i < 0 or i > length(head):
        return head

    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    
    smallHead = updateR(head.next, i - 1, data)
    head.next = smallHead
    return head

def deletei(head, i):
    if i >= length(head):
        return head
    count = 0
    prev = None
    curr = head

    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    if prev is not None:
        prev.next = curr.next
        curr.next = None
    else:
        head = head.next
    return head

#delete using recursion
def deleteiR(head, pos):
    if head is None:
        return None
    if pos == 0:
        return head.next
    smallHead = deleteNodeRec(head.next, pos - 1)
    head.next = smallHead

    return head
    
head = createOpt()
read(head)
head = updateR(head, 2, 8)
read(head)
head = updateR(head, 0, 9)
read(head)
head = updateR(head, 10, 10)
read(head)
