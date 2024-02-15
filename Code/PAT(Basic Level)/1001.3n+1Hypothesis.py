def callatz(n=int(input())):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 5
    if n % 2 == 0:
        return 1 + callatz(n // 2)
    else:
        return 1 + callatz((3 * n + 1) // 2)


print(callatz())
