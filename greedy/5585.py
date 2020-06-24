def greedy(change):
    count = 0
    amount = change
    denoms = [500, 100, 50, 10, 5, 1]
    for denom in denoms:
        if amount % denom >= 0 and amount >= denom:
            quotient = amount // denom
            count += quotient
            amount -= denom * quotient
    return count

change = 1000 - int(input())
print(greedy(change))