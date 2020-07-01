female, male, internship = input().split()
female = int(female)
male = int(male)
internship = int(internship)

team_female = female // 2
team_male = male
team = min(team_female, team_male)

def calc_remain(team):
    remain_female = female - 2*team
    remain_male = male - team
    return remain_female + remain_male

while calc_remain(team) < internship:
    team -= 1

print(team)