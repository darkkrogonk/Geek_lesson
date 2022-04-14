'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из 
  этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.)
'''


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    suma = 0
    my_list_3 = []
    for number in my_list:
        i = number
        result = 0
        while i > 0:
            j = i % 10
            i = i // 10
            result += j
        if result % 7 == 0:
            my_list_3.append(number)
            suma += number


    return suma  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    suma = 0
    for number in my_list:
        i = number + 17
        result = 0
        while i > 0:
            j = i % 10
            i = i // 10
            result += j
        if result % 7 == 0:
            suma += number

    return suma  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    for i in range(1,1000 + 1, 2):
        my_list.append(i**3)

    result_1 = sum_list_1(my_list)
    print(result_1)

    result_2 = sum_list_2(my_list)
    print(result_2)
