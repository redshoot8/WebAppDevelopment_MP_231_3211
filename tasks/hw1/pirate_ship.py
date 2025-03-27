n, m = [int(num) for num in input().split()]
treasures = []

for _ in range(m):
    s = input().split()
    treasure = {}
    treasure['name'] = s[0]
    treasure['weight'] = int(s[1])
    treasure['price'] = int(s[2])
    treasures.append(treasure)

for treasure in treasures:
    if treasure['weight'] > n:
        treasure['price'] = treasure['price'] * (n / treasure['weight'])
        treasure['weight'] = n

for treasure in sorted(treasures, key=lambda x: x['price']):
    print(f'{treasure['name']} {treasure['weight']:.2f} {treasure['price']:.2f}')
