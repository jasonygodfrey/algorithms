class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        curr = prev.next
        for i in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
""" Here is the explanation for the code above:
1. The idea is to find the node before the reversed sublist and the node of the reversed sublist. The node before the reversed sublist will be used to connect with the reversed sublist. The node of the reversed sublist will be used to connect with the rest of the list.
2. The first for loop is used to find the node before the reversed sublist. The second for loop is used to reverse the sublist. """ 