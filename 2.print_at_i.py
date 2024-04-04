
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    while head is not None and head.data != -1:
        count += 1
        head = head.next
    return count

def lengthR(head):
    
    if head:
        return 1 + lengthR(head.next)
    return 0

#prints the element at ith position
def printi(head, i):
    if i >= length(head):
        return ''
    count = 0
    curr = head
    if i == 0:
        return head.data
    while count < i:
        curr = curr.next
        count += 1
    return curr.data


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1
    #j = int(stdin.readline().rstrip())
    #return head, j
    return head


t = int(stdin.readline().rstrip())
result = []
while t > 0:

    #head, i = takeInput()
    head = takeInput()
    #result.append(printi(head, i))
    result.append(lengthR(head))

    t -= 1

for i in range(len(result)):
    print(result[i])
