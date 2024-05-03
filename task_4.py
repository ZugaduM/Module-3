def test(*param1, **param2):
  print('This is param 1: ', param1)
  print("This is param 2: ", param2)


test('first parameter is ', 4, True, 'Today is', 1, 5, 2024, second_parameter=3, today='wednesday')


def recursion_func(faktorial_number):
  if faktorial_number == 1:
    return faktorial_number
  else:
    return faktorial_number * recursion_func(faktorial_number - 1)


print(recursion_func(int(input('Enter number: '))))
