# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def countLength(self,head):
        count=0
        while head:
            head=head.next
            count+=1
        return count
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        n=self.countLength(head)
        k%=n
        if k==0:
            return head
        count=n-k-1
        oldHead=head
        for i in range(count):
            head=head.next
        newHead=head.next
        head.next=None
        lastNodeOfTheLeft=newHead
        while lastNodeOfTheLeft.next:
            lastNodeOfTheLeft=lastNodeOfTheLeft.next
        lastNodeOfTheLeft.next=oldHead
        return newHead

        
        