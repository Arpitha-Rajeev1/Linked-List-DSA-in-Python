#Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
# 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
#Example :
#Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

#For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

#For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def kReverse(head, k):
    if head is None or k == 0:
        return head
    current = head
    next = None
    prev = None
    count = 0

    while(current is not None and count < k):
        
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next is not None:
        head.next = kReverse(next, k)

    return prev



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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
