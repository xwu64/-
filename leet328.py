# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        oddHead = head
        evenHead = head.next
        eH = evenHead

        while 1:
            if oddHead is None or oddHead.next is None or evenHead is None or evenHead.next is None: break
            oddHead.next = oddHead.next.next
            evenHead.next= evenHead.next.next
            oddHead = oddHead.next
            evenHead = evenHead.next
        oddHead.next = eH
        return head
