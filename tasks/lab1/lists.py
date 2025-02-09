n = int(input())
arr = []

for _ in range(n):
    command = input().split()
    match command[0]:
        case 'insert':
            arr.insert(int(command[1]), int(command[2]))
        case 'print':
            print(arr)
        case 'remove':
            arr.remove(int(command[1]))
        case 'append':
            arr.append(int(command[1]))
        case 'sort':
            arr.sort()
        case 'pop':
            arr.pop()
        case 'reverse':
            arr.reverse()
