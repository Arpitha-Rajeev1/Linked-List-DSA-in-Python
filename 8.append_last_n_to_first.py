
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def appendLastNToFirst(head, n, length):
    if head is None or n == 0:
        return head
    if length <= n:
        return
    count = 0
    m = length - n
    newHead = head
    first = None
    print(m)
    while count < m:
        if first is None:
            first = head
        else:
            first = first.next
        newHead = newHead.next
        count += 1
    first.next = None
    newTail = newHead
    while newTail.next is not None:
        newTail = newTail.next
    newTail.next = head
    return newHead

#OR - more simpler but will not work if n > length of LL
def appendLastNToFirsts(head, n):
    if head is None or n == 0:
        return head

    fast = head
    slow = head
    initialHead = head

    for i in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next
        
    temp = slow.next
    slow.next = None
    fast.next = initialHead
    head = temp
    return head

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head, len(datas) - 1


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head, length = takeInput()
    n = int(stdin.readline().rstrip())

    #head = appendLastNToFirst(head, n, length)
    head = appendLastNToFirsts(head, n)
    printLinkedList(head)

    t -= 1 
