# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).

try:
    a = float(input("Введите число A: "))
    n = int(input("Введите целое число больше 0: "))

    result = 1
    for i in range(n):
        result *= a

    print(f"{a} в степени {n} = {result}")

except:
    print('Неверный ввод')