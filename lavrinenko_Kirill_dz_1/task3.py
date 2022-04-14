'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string():
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода

    for proc in number:
        i = proc
        i = i % 10
        # print(proc)
        if proc >= 11 and proc <= 14:
            string = f'{proc} процентов'
        else:
            if i == 1:
                string = f'{proc} процент'
            elif i >= 2 and i < 5:
                string = f'{proc} процента'
            elif i >= 5 and i <= 10 or i == 0:
                string = f'{proc} процентов'
    print(string)

if __name__ == '__main__':
    number = []
    for n in range(1, 101, 1):  # по заданию учитываем только значения от 1 до 100
        number.append(n)
        transform_string()


