'''Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
реализации позже. Главное: дополнить числа до двух разрядов нулём!'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list1 = []

for i in my_list:
    if i.isdigit():
        if len(i) == 1:
            my_list1.extend([f'"0{i}"'])
        else:
            my_list1.extend([f'"{i}"'])
    elif i.find('+') != -1 or i.find('-') != -1:
        if len(i) == 2:
            my_list1.extend([f'"{i[0]}0{i[1]}"'])
        else:
            my_list1.extend([f'"{i}"'])
    else:
        my_list1.append(i)

print(my_list1)
print(" ".join(my_list1))
# print(help(my_list))
