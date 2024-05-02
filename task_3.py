def my_sum(n, *params, txt='Сумма чисел:'):
    s = 0
    for i in range(len(params)):
        s += params[i] ** n
    print(txt, s)


my_sum(1, 1, 2, 3, 4, 5)
my_sum(3, 1, 2, 3, 4, 5)

