import sys

def greedy(meetings):
    meeting_count = 0
    start_time = 0

    for meeting in meetings:
        if meeting[0] >= start_time:
            start_time = meeting[1]
            meeting_count += 1

    return meeting_count

n = int(sys.stdin.readline())
meetings = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings = sorted(meetings, key=lambda time: time[0]) # (start, end) 중 0번째 즉 start time 순 정렬
meetings = sorted(meetings, key=lambda time: time[1]) # (start, end) 중 1번째 즉 end time 순 정렬
print(greedy(meetings))