def calc_fact(n):
    if n == 0:
        return 1

    return n * calc_fact(n - 1)


num = int(input())
print(calc_fact(num))