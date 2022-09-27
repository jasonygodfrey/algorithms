# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return head.next
    """ Here is the explanation for the code above:
1. We create a dummy head for the output list. We also create a variable curr that points to the current node in the output list. We also create a variable carry that will store the carry over digits from the addition of two numbers.
2. We iterate through the input lists and the carry variable until all the nodes in the input lists are exhausted and the carry variable is 0. We check for the carry variable in the while loop condition to ensure that we add a node with the carry variable's value to the output list when the carry variable is not 0.
3. If the input lists are not exhausted, we add the node's value to the carry variable and move to the next node in the list.
4. We create a new node in the output list and add the carry variable's value to the new node. We then move the curr pointer to the new node.
5. We divide the carry variable by 10 to get the carry over digit.
6. We return the dummy head's next node as the output list. """