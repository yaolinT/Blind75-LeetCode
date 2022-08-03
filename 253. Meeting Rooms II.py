# Given an array of meeting time intervals 
# consisting of start and end times 
# [[s1,e1],[s2,e2],…] (si < ei), 
# find the minimum number of conference rooms required.
# Note: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.
###############################################################
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Explaination: we need two meeting rooms
# room 1: [0, 30]; room 2: [5, 10],[15, 20]

# Input: [[7,10],[2,4]]
# Output: 1
###############################################################

# approach 1(Sort by Start, O(nlogn))
# reference: https://www.youtube.com/watch?v=FdzJmTCVyJU
# def minMeetingRooms(self, intervals: List[List[int]]) -> bool:
def minMeetingRooms(intervals):
    start, end = sorted([i[0] for i in intervals]), sorted([i[1] for i in intervals])
    temp, count, startpos, endpos = 0, 0, 0, 0
    while startpos < len(intervals):
        if start[startpos] < end[endpos]:
            startpos += 1
            count += 1
        else:
            endpos += 1
            count -= 1
        temp = max(temp, count)
    return temp

## Driver code
if __name__=='__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    print(minMeetingRooms(intervals))