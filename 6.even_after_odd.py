from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    if head is None:
        return head
    eh, et, oh, ot = None, None, None, None
    while head is not None:
        if head.data % 2 != 0:
            if ot is None:
                ot = head
                oh = head
            else:
                ot.next = head
                ot = head
        else:
            if et is None:
                eh = head
                et = head
            else:
                et.next = head
                et = head
        head = head.next

    if oh is None:
        return eh
    if et is not None:
        et.next = None
    ot.next = eh
    return oh
























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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
