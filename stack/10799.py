import sys
tasks = list(sys.stdin.readline().rstrip())
count = 0
stack = []

for i in range(len(tasks)):
    if tasks[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if tasks[i-1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)