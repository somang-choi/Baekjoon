number_of_people = int(input())
waiting_times = list(map(int, input().split()))
result = 0
waiting_times.sort()

for i in range(number_of_people):
    result += waiting_times[i] * (number_of_people - i)

print(result)