"""
import sys

def search(dest, buttons):
    result = abs(dest - START_CHANNEL) # CASE1: 시작 채널에서 +, - 버튼만 사용하여 목표 채널로 이동
    for num in range(1000001):
        num = str(num)
        for j in range(len(num)):
            if num[j] not in buttons:
                break
            elif j == len(num) -1:
                result = min(result, abs(dest - int(num) + len(str(num))))
    return result

START_CHANNEL = 100

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
buttons = {str(i) for i in range(10)}rcmd
if m != 0:
    buttons -= set(map(str, input().split()))

result = search(n, buttons)
print(result)
"""