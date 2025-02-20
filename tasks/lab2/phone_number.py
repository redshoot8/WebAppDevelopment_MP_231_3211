def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            if len(l[i]) == 10:
                l[i] = f'+7 ({l[i][0:3]}) {l[i][3:6]}-{l[i][6:8]}-{l[i][8:]}'
            else:
                l[i] = f'+7 ({l[i][1:4]}) {l[i][4:7]}-{l[i][7:9]}-{l[i][9:11]}'
        return f(l)
    return fun


@wrapper
def sort_phone(l):
    return sorted(l)


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
