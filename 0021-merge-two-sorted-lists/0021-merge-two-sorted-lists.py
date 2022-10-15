# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next  = l2
                l2 = l2.next
            tail =  tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        
        return dummy.next
    """ Here is the explanation for the code above:
1. The dummy node is used to simplify some corner cases such as a list with only one node, or empty list. On the other hand, the dummy is used to build up the result list.
2. We need two pointers, l1 and l2, to traverse the lists l1 and l2.
3. The tail pointer is used to build up the result list.
4. We compare the two nodes pointed by l1 and l2, and append the node with a smaller value to the result list.
5. We then advance the pointer of the list that we just appended.
6. The while loop terminates when either l1 or l2 points to None.
7. We then append the non-None list to the result list and return the result. """
            #time complexity O(n+m) where n and m are the length of the two lists 
        # space complexity O(1) since we are not using any extra space