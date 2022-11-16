# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
    """ Here is the explanation for the code above:
1. First, we will create a dummy node and make it point to head of the list.
2. Next, we will create two pointers left and right. Both of them will point to the dummy node.
3. After that, we will move the right pointer to the nth position from the first node.
4. Then, we will move both pointers one node at a time until the right pointer reaches the end of the list.
5. At this point, the left pointer will be pointing to the (n+1)th node from the end of the list.
6. Now, all we have to do is to make the next pointer of the left node point to the (n+1)th node’s next node.
7. Finally, we will return the next node of the dummy node. """