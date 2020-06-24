def greedy(denoms, amount):
    count = 0
    denoms = list(reversed(denoms))
    total = amount

    for coin in denoms:
        if total % coin >= 0 and total >= coin:
            quotient = total // coin
            count += quotient
            total -= quotient * coin
        if total == 0:
            break

    return count

n, amount = list(map(int, input().split()))
denoms = []
for i in  range(n):
    coin = int(input())
    if coin > amount:
        break
    denoms.append(coin)
print(greedy(denoms, amount))