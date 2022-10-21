class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
        


        #time complexity O(nlogn)
        # space complexity O(1)
""" Here is the explanation for the code above:
1. We sort the list of intervals by the start time of each interval.
2. We iterate through the list of intervals and check if each end time is less than or equal to the start time of the next interval.
3. If the end time is greater than the start time of the next interval, we return False.
4. If we reach the end of the list, we return True. """