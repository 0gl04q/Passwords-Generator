from random import *


# проверка длинны пароля
def is_len(passwd):
    return True if passwd.isdigit() and int(passwd) >= 8 else False


# функция генератора пароля
def passwd_generator():
    passwd_end = ''

    # получаем по одному символу которые обязательно должны присутствовать
    # в зависимости от нашего предыдущего выбора
    if digits in chars:
        passwd_end += choice(digits)
    if lowercase_letters in chars:
        passwd_end += choice(lowercase_letters)
    if uppercase_letters in chars:
        passwd_end += choice(uppercase_letters)
    if punctuation in chars:
        passwd_end += choice(punctuation)

    # создаем список из случайных символов исходя из разницы необходимой длинны с уже полученными символами
    passwd_end = sample(chars, len_passwords - len(passwd_end)) + list(passwd_end)  # объединяем 2 списка

    shuffle(passwd_end)  # перемешиваем

    return ''.join(passwd_end)  # возвращаем пароль строкой


if __name__ == '__main__':

    # основные сведения
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    symbols = 'il1Lo0O'
    chars = ''

    # получение необходимой информации для создания паролей от пользователя
    amount_passwords = int(input('Введите количество паролей: '))

    while True:  # проверка длинны пароля
        len_passwords = input('Введите длину одного пароля: ')
        if is_len(len_passwords):
            len_passwords = int(len_passwords)
            break
        print('Повторите ввод\n')

    if input('Введите "д" если в пароль нужно включить цифры: ').lower() == 'д':
        chars += digits

    if input('Введите "д" если в пароль нужно включить буквы нижнего регистра: ').lower() == 'д':
        chars += lowercase_letters

    if input('Введите "д" если в пароль нужно буквы верхнего регистра: ').lower() == 'д':
        chars += uppercase_letters

    if input('Введите "д" если в пароль нужно включить символы: ').lower() == 'д':
        chars += punctuation

    if input('Введите "д" если в пароль нужно исключить неоднозначные символы: ').lower() == 'д':
        chars = list(chars)  # переводим строку в список
        for ch in symbols:  # исключаем неоднозначные символы
            del chars[chars.index(ch)]
        chars = ''.join(chars)  # возвращаем строку

    print()  # пробел для консоли

    # генерируем список паролей
    passwords_list = [passwd_generator() for _ in range(amount_passwords)]

    # выводим готовые пароли
    print(*passwords_list)
