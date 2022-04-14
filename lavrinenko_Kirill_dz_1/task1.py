"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    total_time = ''
    days = duration // 86400
    hours = duration // 3600
    minuts = duration // 60
    second = duration - minuts * 60

    if duration < 60:
        total_time = f'{second} сек '
    elif duration >= 60 and duration < 3600:
        total_time = f'{minuts} мин {second} сек '
    elif duration >= 3600 and duration < 86400:
        total_time = f'{hours} час {minuts % 60} мин {second % 3600} сек'
    else:
        total_time = f'{days} дн {hours % 24} час {minuts % 60} мин {second % 3600} сек'



    return total_time


def one_cycle_realisation(duration):
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    total_time = ''

    # YOUR CODE HERE
    return total_time


if __name__ == '__main__':
    duration = 8646
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))
