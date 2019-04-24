a,b = (int(x) for x in input().split())

coins = max(a,b)

if a > b:
    a -= 1
else:
    b -= 1

coins += max(a,b)

print(coins)