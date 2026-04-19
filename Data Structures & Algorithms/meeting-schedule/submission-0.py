"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
# Sort by the 'start' attribute of the Interval object
        intervals.sort(key=lambda x: x.start)
        
        for i in range(len(intervals) - 1):
            # Access attributes using .start and .end
            if intervals[i+1].start < intervals[i].end:
                return False
                
        return True