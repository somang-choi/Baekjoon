from itertools import combinations

min_difference = 99999
def calc_power(members):
    power = 0
    for (i, j) in combinations(members, 2):
        power += S[i][j] + S[j][i]
    return power

def calc_min(start, link):
    power_start = calc_power(start)
    power_link = calc_power(link)
    return abs(power_start - power_link)

N = int(input())
S = [0]*N
for i in range(N):
    s = list(map(int, input().split()))
    S[i] = s

members = list(range(N))
teams = combinations(members, N//2)

for team in teams:
    start = list(team)
    link = list(set(members) - set(start))
    result = calc_min(start, link)
    if result < min_difference:
        min_difference = result

print(min_difference)
