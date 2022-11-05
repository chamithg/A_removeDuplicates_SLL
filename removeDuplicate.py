# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummiHead = ListNode()
        dummiHead.next = head
        runner = head
    
        if runner is None:
            return dummiHead.next
        while runner.next!= None:
            while runner.next and runner.val == runner.next.val:
                if runner.next.next:
                    runner.next = runner.next.next
                else:
                    runner.next = None
            if runner.next:
                runner =runner.next
        
        
        return dummiHead.next