n = int(input())
A = input().split()
print(sorted(set(A))[-2] if len(set(A)) > 1 else sorted(set(A))[-1])
