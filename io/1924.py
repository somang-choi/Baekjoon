yoils = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days_for_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = map(int, input().split(' '))
past_days = sum(days_for_month[0:month-1])
days = day + past_days
print(yoils[days%7])