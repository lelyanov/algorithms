# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

print('Задание 6')

import random

rnd_val = random.randint(0, 100)
MAX_COUNT = 10


def question(count: int):
    n = int(input('Введите число: '))
    if n > rnd_val:
        print(f"переборщил (осталось попыток: {MAX_COUNT - count})")
    elif n < rnd_val:
        print(f"недобрал (осталось попыток: {MAX_COUNT - count})")
    else:
        print("Конградьюлешнс!!!")
        return
    if count == MAX_COUNT:
        print(f"Ты сделал все, что мог! Правильный ответ был: {count}")
        return
    question(count + 1)


question(1)
