# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    if head is None:
        return -1
    count = 0
    while head is not None:
        if n == head.data:
            return count
        count += 1
        head = head.next
    return -1
