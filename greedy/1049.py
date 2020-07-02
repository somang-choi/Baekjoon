n, m = map(int, input().split())

selections = []
for i in range(0, m):
    pack, piece = map(int, input().split())
    selections.append((pack, piece))

count_pack = n//6
count_piece = n - 6*count_pack
price_pack = min(selections, key = lambda s: s[0])[0]
price_piece = min(selections, key = lambda s: s[1])[1]

prices = []
for i in range(0, count_pack + 2):
    cnt_pack = i
    cnt_piece = (n - 6*cnt_pack) if (n - 6*cnt_pack) >= 0 else 0
    prices.append(cnt_pack*price_pack + cnt_piece*price_piece)

print(min(prices))