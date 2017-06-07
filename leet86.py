# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None: return head

        tail = None
        tmp = head
        length = 0

        while tmp is not None:
        	tail = tmp
        	tmp = tmp.next
        	length+=1

        cur = head
        previous = None
        #print tail.val
        for _ in xrange(length):
        	if cur.val < x:
        		previous = cur
        		cur = cur.next
        	else:
        		if previous is None:
        			tail.next = cur
        			next = cur.next
        			cur.next = None
        			tail = cur
        			cur = next
        			head = cur

        		else:
        			tail.next = cur
        			previous.next = cur.next
        			cur.next = None
        			tail = cur
        			cur = previous.next
        return head
