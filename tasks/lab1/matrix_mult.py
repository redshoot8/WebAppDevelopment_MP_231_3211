n = int(input())
m1, m2 = [], []

for _ in range(n):
    m1.append([int(num) for num in input().split()])

for _ in range(n):
    m2.append([int(num) for num in input().split()])

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += m1[i][k] * m2[k][j]

for row in range(n):
    print(*result[row])
