from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def swapNodes(head, i, j):
    if head is None or i == j:
        return head
    t, s = 0, 0
    tail = head
    temp1 = None
    if i < j:
        big = j
        small = i
    else:
        big = i
        small = j
    while t < small:
        temp1 = tail
        tail = tail.next
        t += 1
    take = tail
    while s < big - small:
        temp2 = take
        take = take.next
        s += 1

    if big - small == 1 and temp1 is None:
        tail.next = take.next
        head = take
        take.next = tail
        return head

    if temp1 is not None:
        temp1.next = take
    if temp1 is None:
        head = take
    stop = take.next
    if big - small == 1:
        start = tail
    else:
        start = tail.next
        temp2.next = tail

    tail.next = stop
    take.next = start

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

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
