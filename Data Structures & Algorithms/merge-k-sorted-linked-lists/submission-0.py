class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        box = []

        for item in lists:
            cur = item
            while cur:
                box.append(cur.val)
                cur = cur.next

        if not box:
            return None

        box.sort()

        dummy = ListNode(0)
        cur = dummy

        for val in box:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next