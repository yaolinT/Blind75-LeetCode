# You are given an array of k linked-lists lists, 
# each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
###############################################################
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Input: lists = []
# Output: []

# Input: lists = [[]]
# Output: []
###############################################################

# approach 1
# reference: https://www.youtube.com/watch?v=q5a5OiGbT6Q
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeKLists(self, lists):
        # lists = [[1,4,5]]
        # print(len(lists))
        if not lists or len(lists) == 0: return None
        
        while len(lists) > 1:
            flist = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # print(list1)
                list2 = lists[i+1] if len(lists) > (i+1) else None
                # print(list2)
                flist.append(self.mergeTwoLists(list1, list2))
            lists = flist 
        return lists[0]
            
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
        if list2:
            r.next = list2
        return l.next
        
## Driver code
if __name__=='__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    print(Solution().mergeKLists(lists))