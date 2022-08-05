# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
###############################################################
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [], list2 = []
# Output: []

# Input: list1 = [], list2 = [0]
# Output: [0]
###############################################################

# approach 1
# reference: https://www.youtube.com/watch?v=XIdigk956u0
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1, list2):
        l = ListNode()
        r = l
        while list1 and list2:
            if list1.val <= list2.val:
                r.next = list1
                list1 = list1.next
            else:
                r.next = list2
                list2 = list2.next
            r = r.next
        if list1:
            r.next = list1
        else:
            r.next = list2
        return l.next

## Driver code
if __name__=='__main__':
    list1 = [1,2,4]
    list2 = [1,3,4]
    print(Solution().mergeTwoLists(list1, list2))