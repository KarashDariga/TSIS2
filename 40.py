c = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(len(a)):
    c.append(a[i]+b[i])

print(c)
