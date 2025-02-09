n = int(input())
passenger_times = []

for _ in range(n):
    passenger_times.append([int(num) for num in input().split()])
    
t = int(input())
count = 0

for time in passenger_times:
    if time[0] <= t <= time[1]:
        count += 1
        
print(count)
