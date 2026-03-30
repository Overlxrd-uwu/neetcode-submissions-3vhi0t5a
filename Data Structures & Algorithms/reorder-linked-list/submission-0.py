# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# so the idea and the mathmatical logic is following the [0,n-1,1,n-2....]
# if n = 4 [0,3,1,2] n=5 [0,4,1,3,2] n=6 [0,5,1,4,2,3]
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # f -> l -> f.next -> l.prev -> f.next.next ......
        if not head or not head.next:
            return

        # 1) find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2) reverse second half
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev is the head of reversed second half
        second = prev

        # 3) merge two halves
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2