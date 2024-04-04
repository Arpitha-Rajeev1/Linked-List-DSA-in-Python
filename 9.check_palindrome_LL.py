
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def reverse3(head):
    if head is None or head.next is None:
        return head
    smallHead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead


def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow = head
    fast = head
    if fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    temp = slow.next
    smallHead = reverse3(temp)
    while smallHead is not None and head is not None:
        if smallHead.data != head.data:
            return False
        smallHead = smallHead.next
        head = head.next
    return True
































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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1
