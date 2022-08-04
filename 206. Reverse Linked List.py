# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.
###############################################################
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
###############################################################

# approach 1 (Exchange)
# reference: https://www.youtube.com/watch?v=G0_I-ZF0S38
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = None, head
        while r != None:
            next = r.next
            r.next = l
            l = r
            r = next
        return l

# approach 2 (Recursion)
# reference: https://ithelp.ithome.com.tw/articles/10271920
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        if not head: return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)

## Driver code
# if __name__=='__main__':
#      ListNode()
#     head = [1,2,3,4,5]
#     print(Solution().reverseList(head))