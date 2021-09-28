# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode()
        tmp = ans
        up = 0
        
        while l1 or l2 or up:
            l1_val = 0
            l2_val = 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            num = l1_val + l2_val + up
            
            if num > 9:
                tmp.next = ListNode(num%10)
                tmp = tmp.next
                up = 1
            else:
                tmp.next = ListNode(num)
                tmp = tmp.next
                up = 0
            
        return ans.next