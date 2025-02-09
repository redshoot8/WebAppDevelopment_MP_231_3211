import pandas as pd

df = pd.read_csv('tasks/lab1/files/products.csv')

print(f'{df['Взрослый'].sum():.2f}')
print(f'{df['Пенсионер'].sum():.2f}')
print(f'{df['Ребенок'].sum():.2f}')
