def test():
    a = 'this is a'
    b = 'this is b'
    print(f'a = {a}, b = {b}')


def test2(var_a=1, var_b=2, var_c=3):
    print(f'My params are: {var_a}, {var_b}, {var_c}')


test()
test2()
