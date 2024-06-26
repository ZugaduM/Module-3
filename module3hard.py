data_structure = [                                        # начальный список
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
  "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(struct):                      # объявляем функцию, которая возвращает сумму всех символов в передаваемом списке
    count = 0                                             # объявляем переменную для хранения количества посчитанных символов
    for item in struct:                                   # создаем цикл for для перебора элементов списка
        if isinstance(item, list | tuple | set):          # проверка на вложенные структуры (списки, кортежи, множества)
          count += calculate_structure_sum(item)          # используем рекурсию для распаковки списков разной вложенности и результат прибавляем к счетчику count
        if isinstance(item, dict):                        # проверка на принадлежность к типу словарь
          for i in item:                                  # создаем цикл for для перебора ключей словаря
            count += len(i)                               # прибавляем к счетчику count количество символов в ключе
          count += sum(item.values())                     # прибавляем к счетчику count сумму значений словаря
        if isinstance(item, int):                         # проверка на принадлежность к целочисленному типу
          count += item                                   # прибавляем к счетчику count целочисленное значение
        if isinstance(item, str):                         # проверка на принадлежность к строковому типу
          count += len(item)                              # прибавляем к счетчику count количество символов в строке

    return count                                          # возвращаем посчитанное количество символов



result = calculate_structure_sum(data_structure)          # вызываем функцию и передаем структуру данных (словарь и т.д.) как аргумент, результат присваиваем переменной result
print(result)                                             # выводим в консоль значение переменной result
