#Given a Singly Linked List of integers, delete all the alternate nodes in the list.
#Example:
#List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
#Alternate nodes will be:  20, 40, and 60.

#Hence after deleting, the list will be:
#Output: 10 -> 30 -> 50 -> null
#Note :
#The head of the list will remain the same. Don't need to print or return anything.
#Input format :
#The first and the only line of input will contain the elements of the Singly Linked List separated by a single space and terminated by -1.
#Output Format :
#The only line of output will contain the updated list elements.
#Input Constraints:
#1 <= N <= 10 ^ 6.
#Where N is the size of the Singly Linked List

#Time Limit: 1 sec
#Sample Input 1:
#1 2 3 4 5 -1
#Sample Output 1:
#1 3 5
#Explanation of Sample Input 1:
#2, 4 are alternate nodes so we need to delete them 
#Sample Input 2:
#10 20 30 40 50 60 70 -1
#Sample Output 2:
#10 30 50 70

def deleteAlternateNodes(head):
    if (head is None):
        return

    node = head.next

    if (node is None):
        return

    # Change the next link of head
    head.next = node.next

    deleteAlternateNodes(head.next)
