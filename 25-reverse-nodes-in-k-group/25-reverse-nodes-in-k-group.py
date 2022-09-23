# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 1:
            return head
        count = 0
        curr = head
        while curr and count != k:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
                count -= 1
            head = curr
        return head        
    """ Here is the explanation for the code above:
1. First we will check if the head is null or not. If it is null, we will return null.
2. Then we will check if k is equal to 1 or not. If it is equal to 1, we will return head.
3. We will create a count variable and a curr variable. We will assign the count variable to 0.
4. We will assign the curr variable to head.
5. We will create a while loop where we will check if curr is not null and count is not equal to k.
6. We will increment the value of curr and count by 1.
7. If the count is equal to k, we will assign the curr variable to the return value of the function with curr as the argument and k as the argument.
8. We will create a while loop where we will check if the value of count is greater than 0.
9. We will create a temp variable and assign it the value of head.next.
10. We will assign the value of head.next to curr.
11. We will assign the value of curr to head.
12. We will assign the value of head to temp.
13. We will decrement the value of count by 1.
14. We will assign the value of head to curr.
15. We will return head.
16. If the count is not equal to k, we will return head. """