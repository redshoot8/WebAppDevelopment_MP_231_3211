import random
import math


def circle_square_mk(r: float, n: int) -> float:
    points = [(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(n)]    
    points_inside = sum(1 for x, y in points if x*x + y*y <= r*r)
    return 4 * r * r * points_inside / n


r = 5.0
n_values = [1000, 10000, 100000, 1000000]

for n in n_values:
    mk_area = circle_square_mk(r, n)  
    exact_area = math.pi * r * r
    error = abs(mk_area - exact_area)
    
    print(f'n = {n:,}')
    print(f'Площадь (Монте-Карло): {mk_area:.6f}')
    print(f'Точная площадь: {exact_area:.6f}')
    print(f'Погрешность: {error:.6f}')
    print(f'Относительная погрешность: {error/exact_area*100:.6f}%\n')
