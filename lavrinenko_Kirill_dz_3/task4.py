'''
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
        },
    "И": {
        "И": ["Илья Иванов"]
        },
    "С": {
            "И": ["Иван Сергеев", "Инна Серова"],
            "А": ["Анна Савельева"]
        }
}
Как поступить, если потребуется сортировка по ключам?
'''


def thesaurus(*args):
  '''  total = {}

    for arg in args:
        if arg[0] not in total.keys():
            total[arg[0]] = list()
            total[arg[0]].append(arg)
        else:
            total[arg[0]].append(arg)
    return total  # YOUR CODE HERE'''
'''
    print(args)
        for i in args:
            i = i.split()
            print(i[-1])
'''


if __name__ == "__main__":
    print(thesaurus("Иван Сергеев", "Инна Серова",
                    "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
