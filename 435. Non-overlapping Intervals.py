# Given an array of intervals intervals 
# where intervals[i] = [starti, endi], 
# return the minimum number of intervals 
# you need to remove to make the rest of the intervals non-overlapping.
###############################################################
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed 
# and the rest of the intervals are non-overlapping.

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] 
# to make the rest of the intervals non-overlapping.

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals 
# since they're already non-overlapping.
###############################################################

# approach 1(Sort by Start, O(nlogn))
# reference: https://www.youtube.com/watch?v=nONCGxWoUfM
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
def eraseOverlapIntervals(intervals):
        intervals.sort()
        temp = 0
        end = intervals[0][1]
        for l, r in intervals[1:]:
            if l >= end:
                end = r
            else:
                temp += 1
                end = min(r, end)
        return temp

## Driver code
if __name__=='__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlapIntervals(intervals))