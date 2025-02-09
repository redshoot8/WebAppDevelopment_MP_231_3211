n, m = [int(num) for num in input().split()]
arr = [int(num) for num in input().split()]

happiness = 0

A = set([int(num) for num in input().split()])
B = set([int(num) for num in input().split()])

for elem in A:
    if elem in arr:
        happiness += 1
    
for elem in B:
    if elem in arr:
        happiness -= 1

print(happiness)
