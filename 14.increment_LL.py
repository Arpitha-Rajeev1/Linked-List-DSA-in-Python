#Given a large number represented in the form of a linked list. Write code to increment the number by 1 in-place(i.e. without using extra space).
#Note: You don't need to print the elements, just update the elements and return the head of updated LL.
#Input Constraints:
#1 <= Length of Linked List <=10^6.
#Input format :
#Line 1 : Linked list elements (separated by space and terminated by -1)
#Output Format :
#Line 1: Updated linked list elements 
#Sample Input 1 :
#3 9 2 5 -1
#Sample Output 1 :
#3 9 2 6
#Sample Input 2 :
#9 9 9 -1
#Sample Output 1 :
#1 0 0 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse3(head):
    if head is None or head.next is None:
        return head

    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def nextNumber(head):
    if head is None:
        return head
    smallHead = reverse3(head)
    curr = smallHead
    flag = True

    while curr is not None and flag:
        if curr.next is None and curr.data == 9:
            curr.data = 1
            temp = Node(0)
            temp.next = smallHead
            smallHead = temp
            curr = curr.next
        elif curr.data == 9:
            curr.data = 0
            curr = curr.next
        else:
            curr.data += 1
            curr = curr.next
            flag = False
    head = reverse3(smallHead)
    return head

        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)
