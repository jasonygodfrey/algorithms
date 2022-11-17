# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
                return None
        while len(lists) > 1:
            mergedLists= []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
        
        
        
        
    def mergeList(self, l1, l2):
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
1. We have to check if the list is empty or None. If it is, return None
2. We have to keep merging the lists until there is only one list left
3. Then we return the only list left
4. We have a function that merges two lists
5. We have a dummy node to point to the head of the list
6. We have a tail node to point to the last node of the list
7. We use a while loop to check if l1 or l2 is empty.
8. If l1 is not empty and l2 is not empty, we compare the values of l1 and l2
9. If l1 is smaller than l2, we add l1 to the list and move l1 to l1.next
10. Otherwise, we add l2 to the list and move l2 to l2.next
11. We move the tail to tail.next
12. We check if l1 is empty or l2 is empty. If l1 is empty, we add l2 to the list. If l2 is empty, we add l1 to the list.
13. We return dummy.next which is the head of the merged list
14. """
            