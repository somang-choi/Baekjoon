import sys, math
N = int(input())

count_cards = {} # 정수 범위가 너무 커서 dictionary 사용
for i in range(N):
    card = int(sys.stdin.readline().rstrip())
    if card in count_cards:
        count_cards[card] += 1
    else:
        count_cards[card] = 1

sorted_cards = sorted(count_cards.items(), key=lambda x: (-x[1], x[0]))
print(sorted_cards[0][0])