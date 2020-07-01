import sys

def generate_applicants():
    applicants = []
    for i in range(0, n):
        paper, interview = map(int, sys.stdin.readline().split())
        applicants.append((paper, interview))
    applicants = sorted(applicants)
    return applicants

def greedy():
    count = 1
    min_interview_score = applicants[0][1]
    for i in range(1, n):
        interview_score = applicants[i][1]
        if interview_score < min_interview_score:
            min_interview_score = interview_score
            count += 1
    return count

t = int(sys.stdin.readline())
for i in range(0, t):
    n = int(sys.stdin.readline())
    applicants = generate_applicants()
    print(greedy())
