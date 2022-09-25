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
