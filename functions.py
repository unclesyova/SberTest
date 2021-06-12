"""Модуль, содержащий две функции dict_to_str() и sort_by_freq()."""

from collections import defaultdict

def dict_to_str(dictionary):
    """Функция принимает словарь и преобразует его в строку.

    Словарь использует буквы как ключи и позиции этих букв как значения.
    Результирующая строка состоит из букв-ключей словаря на указанных в
    значениях позициях.
    """
    inversed_dict = {}
    # поменять местами значения и ключи словаря
    for key, value in dictionary.items():
       for val in value:
           inversed_dict[val] = key
    # преобразовать словарь в список кортежей (ключ, значение)
    # и отсортировать по ключу
    sorted_by_key = sorted(inversed_dict.items(), key=lambda x: x[0])
    # объединить значения в один список и построить строку с помощью join
    result = "".join(list(zip(*sorted_by_key))[1])  

    return result 



def sort_by_freq(num_lst):
    """Функция принимает список чисел и сортирует их по частоте появления.

    При равной частоте числа сортируются в порядке появления в исходном
    списке. Возвращает отсортированный список.
    """
    # отслеживать числа по частоте и по порядку появяления с помощью двух словарей
    freq_dict = defaultdict(int)
    order_dict = {}
    for i, num in enumerate(num_lst):
        freq_dict[num] += 1
        try:
            order_dict[num]
        except KeyError:
            order_dict[num] = len(num_lst) - i
    num_lst.sort(key=lambda x: (freq_dict[x], order_dict[x]), reverse=True)
    
    return num_lst 
