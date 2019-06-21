
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print('Задание 9')

amountNumbers = int(input('Сколько чисел собрался вводить? '))

n = 1
max_number = ""
max_sum = 0

while n <= amountNumbers:
    number_str = input(f'Введите {n} число: ')
    number = int(number_str)
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    if sum > max_sum:
        max_sum = sum
        max_number = number_str
    n += 1

print(f"Максимальное число: '{max_number}', его сумма = {max_sum}")