'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
'''


def num_translate(number: str):
    # YOUR CODE HERE
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
            return value  # YOUR CODE HERE


if __name__ == "__main__":
    print(num_translate('one'))
    print(num_translate('six'))


