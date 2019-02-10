"""*Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
* """
class MeetingRooms(object):
    def minrooms(self, meetings):
        n = len(meetings)
        start = []
        end = []

        for i in range(n):
            start.append(meetings[i][0])
            end.append(meetings[i][1])

        start.sort()
        end.sort()

        rooms = 0
        free = 0
        for i in range(0, n):
            if start[i] < end[free]:
                rooms += 1
            else:
                free += 1
        return rooms  # return rooms important

meet = MeetingRooms()
meeting = [[0, 30], [5, 10], [15, 20]]
meeting1 = [[7, 10], [2, 4]]
print(meet.minrooms(meeting))
print(meet.minrooms(meeting1))
