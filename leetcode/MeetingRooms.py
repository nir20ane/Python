"""* Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.
Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
*"""
class MeetingRooms(object):
    def canattend(self, meetings):
        n = len(meetings)
        start = []
        end = []

        for i in range(n):
            start.append(meetings[i][0])
            end.append(meetings[i][1])

        start.sort()
        end.sort()

        for i in range(1, n):
            if start[i] < end[i-1]:
                return False
        return True

meet = MeetingRooms()
meeting = [[0, 30], [5, 10], [15, 20]]
meeting1 = [[7, 10], [2, 4]]
print(meet.canattend(meeting))
print(meet.canattend(meeting1))
