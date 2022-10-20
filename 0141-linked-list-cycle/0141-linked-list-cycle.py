# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast= head, head
        
        while fast  and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        
        return False
        #time complexity O(n)
        # space complexity O(1)

        """ Here is the explanation for the code above:
1. In this code, I am going to use the two pointers method to solve this problem.
2. I will have a slow pointer that will move one step at a time, and a fast pointer that will move two steps at a time. 
3. If there is a cycle in the linked list, then the fast pointer will eventually meet the slow pointer. 
4. If there is no cycle, the fast pointer will eventually reach the end of the linked list, and the while loop will terminate. 
5. In the end, I will return whether or not the fast pointer has met the slow pointer. """