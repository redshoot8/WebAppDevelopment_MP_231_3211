n = int(input())
records = []

for i in range(n):
    records.append([])
    records[i].append(input())
    records[i].append(float(input()))

sorted_records = sorted(records, key=lambda x: (x[1], x[0]))
scores = sorted(set(map(lambda x: x[1], records)))

for record in sorted_records:
    if record[1] == scores[1]:
        print(record[0])
