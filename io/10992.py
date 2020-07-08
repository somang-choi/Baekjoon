n = int(input())
if n == 1:
    print('*')
for i in range(1, n):
    if i == 1:
        print((n-i)*' ' + '*')
    if i == n-1:
        print((2*n - 1)*'*')
        break
    print((n-i-1)*' ' + '*' + (2*i - 1)*' ' + '*')

