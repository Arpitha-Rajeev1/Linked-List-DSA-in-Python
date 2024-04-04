#O(n^2)
def reverse1(head):
    if head is None or head.next is None:
        return head
    smallHead = reverse1(head.next)
    curr = smallHead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallHead

#O(n)
def reverse2(head):
    if  head is None or head.next is None:
        return head
    smallHead, smallTail = reverse2(curr.next)
    smallTail.next = curr
    curr.next = None
    return smallHead, curr

#O(n) with only one return
def reverse3(head):
    if  head is None or head.next is None:
        return head
    smallHead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead

#iterative
def reverse(head):
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
