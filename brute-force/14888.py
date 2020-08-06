from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

op_list = []
op_list += [1] * plus
op_list += [2] * minus
op_list += [3] * multiple
op_list += [4] * division

op_set = list(set(permutations(op_list)))

max_answer = -1000000001
min_answer = 1000000001

def calc(ans, num, op_idx):
    if op_idx == 1:
        ans += num
    elif op_idx == 2:
        ans -= num
    elif op_idx == 3:
        ans *= num
    elif op_idx == 4:
        if ans < 0:
            ans = -((-ans) // num)
        else:
            ans //= num
    return ans

for case in op_set:
    answer = A[0]

    for i in range(N-1):
        answer = calc(answer, A[i+1], case[i])

    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)