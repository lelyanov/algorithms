# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

print('Задание 5')

i = 32
MAX_COUNT = 127
MAX_STR_COUNT = 10

while i <= MAX_COUNT:
    new_str = ""
    n = 1
    while i <= MAX_COUNT and n <= MAX_STR_COUNT:
        new_str += f"{chr(i)}\t"
        if i != MAX_COUNT and n != MAX_STR_COUNT:
            new_str += "|\t"
        n += 1
        i += 1
    print(new_str)
