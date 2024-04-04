#You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
#To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

#Sample Input 1 :
#1
#1 2 3 4 5 6 7 8 -1
#2 2
#Sample Output 1 :
#1 2 5 6

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
    if head is None or (m !=0  and n == 0):
        return head
    if m == 0:
        return
    temp = head
    tail = None
    roll = head
    while roll is not None:
        count = 0
        while count < m and temp is not None:
            if tail is None:
                tail = head
            else:
                tail = tail.next
            temp = temp.next
            count += 1
        sum = 0
        while sum < n and temp is not None:
            tail.next = temp.next
            temp = temp.next
            sum += 1
        roll = temp
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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
