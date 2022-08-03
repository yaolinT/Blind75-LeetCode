# Given an array of meeting time intervals consisting of start 
# and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.
# Note: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.
###############################################################
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: False

# Input: intervals = [[7,10],[2,4]]
# Output: True
###############################################################

# approach 1(Sort by Start, O(nlogn))
# reference: https://www.youtube.com/watch?v=PaJxqZVPhbg
# def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
def canAttendMeetings(intervals):
    intervals.sort(key = lambda i: i[0])
    for i in range(1, len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
           return False
    return True 

## Driver code
if __name__=='__main__':
    intervals = [[0,30],[5,10],[15,20]]
    print(canAttendMeetings(intervals))