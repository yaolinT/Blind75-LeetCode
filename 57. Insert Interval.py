# You are given an array of non-overlapping intervals /intervals/ 
# where intervals[i] = [starti, endi] represent the start 
# and the end of the ith interval 
# and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] 
# that represents the start and end of another interval.
# Insert newInterval into intervals 
# such that intervals is still sorted in ascending order by starti 
# and intervals still does not have any overlapping intervals 
# (merge overlapping intervals if necessary).
# Return intervals after the insertion.
###############################################################
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], 
#        newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] 
# overlaps with [3,5],[6,7],[8,10].
###############################################################

# approach 1(O(n))
# reference: https://www.youtube.com/watch?v=A8NUOmlwOlM
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
def insert(intervals, newInterval):
    temp = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            temp.append(newInterval)
            return temp + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            temp.append(intervals[i])
        else:
            a = min(newInterval[0], intervals[i][0])
            b = max(newInterval[1], intervals[i][1])
            newInterval = [a, b]
    temp.append(newInterval)
    return temp

## Driver code
if __name__=='__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(insert(intervals, newInterval))