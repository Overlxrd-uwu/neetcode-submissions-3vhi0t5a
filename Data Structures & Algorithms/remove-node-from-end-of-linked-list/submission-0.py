class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        if n == length:
            return head.next

        cur = head
        steps = length - n - 1   # move to node before the one to delete

        while steps > 0:
            cur = cur.next
            steps -= 1

        cur.next = cur.next.next
        return head