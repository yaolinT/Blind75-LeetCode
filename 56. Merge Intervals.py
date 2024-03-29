# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.
###############################################################
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, 
# merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
###############################################################

# approach 1(Sort by Start, O(nlogn))
# reference: https://www.youtube.com/watch?v=44H3cEC2fFM
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
def merge(intervals):
    intervals.sort(key = lambda i:i[0])
    temp = [intervals[0]]
    for l, r in intervals[1:]:
        output = temp[-1][1]
        if l <= output:
            temp[-1][1] = max(output, r)
        else:
            temp.append([l, r])
    return temp

## Driver code
if __name__=='__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))