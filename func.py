def func(n):
    if n == 1:
        return 1
    else:
        a = 1
        for i in range(1, n+1):
            a = i * a
        return a


if __name__ == '__main__':
    print(func(6))