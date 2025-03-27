import pandas as pd

df = pd.read_csv('tasks/hw1/files/products.csv')

print(f'{df['Взрослый'].sum():.2f}')
print(f'{df['Пенсионер'].sum():.2f}')
print(f'{df['Ребенок'].sum():.2f}')

# import csv

# a = 0
# p = 0
# c = 0

# with open('tasks/lab1/files/products.csv', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     next(reader)
    
#     for row in reader:
#         a += float(row[1])
#         p += float(row[2])
#         c += float(row[3])

# print(f'{a:.2f}')
# print(f'{p:.2f}')
# print(f'{c:.2f}')
