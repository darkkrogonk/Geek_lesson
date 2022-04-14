'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''


def num_translate_adv(number: str):
    numbers = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}

    for key, value in numbers.items():
        if key == number:
            return value
        if key.title() == number:
            return value.title()
            # YOUR CODE HERE


if __name__ == "__main__":
    print(num_translate_adv('Five'))
    print(num_translate_adv('seven'))
