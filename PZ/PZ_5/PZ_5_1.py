# Составить функцию, которая выполнит суммирования числового ряда.

while True:
    try:
        x = int(input("Введите послнднее число x: "))
    except ValueError:
        print("Ошибка")
        continue
    break
print(sum([i for i in range(1, x + 1)]))
