# PZ_2
#  def p(x, a, b):
#     c = a / x
#     i = b / x
#     r = c / i
#
#     return c, i, r
#
#
# x = float(input("Введите вес шоколадных конфет в кг: "))
# a = float(input("Введите стоимость шоколадных конфет в рублях: "))
# b = float(input("Введите стоимость ирисок в рублях: "))
#
# c, i, r = p(x, a, b)
#
# print("Стоимость 1 кг шоколадных конфет:", c, "рублей")
# print("Стоимость 1 кг ирисок:", i, "рублей")
# print("Шоколадные конфеты дороже ирисок в", r, "раз")

import tkinter as tk
from tkinter import messagebox


def p(x, a, b):
    c = a / x
    i = b / x
    r = c / i
    return c, i, r


def calculate():
    try:
        x = float(entry_x.get())
        a = float(entry_a.get())
        b = float(entry_b.get())

        c, i, r = p(x, a, b)

        result_c.config(text=f"Стоимость 1 кг шоколадных конфет: {c:.2f} рублей")
        result_i.config(text=f"Стоимость 1 кг ирисок: {i:.2f} рублей")
        result_r.config(text=f"Шоколадные конфеты дороже ирисок в {r:.2f} раз")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")


root = tk.Tk()

label_x = tk.Label(root, text="Введите вес шоколадных конфет в кг:")
label_x.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5, sticky="we")

label_a = tk.Label(root, text="Введите стоимость шоколадных конфет в рублях:")
label_a.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=10, pady=5, sticky="we")

label_b = tk.Label(root, text="Введите стоимость ирисок в рублях:")
label_b.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=10, pady=5, sticky="we")

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_c = tk.Label(root, text="")
result_c.grid(row=4, column=0, columnspan=2, pady=5)
result_i = tk.Label(root, text="")
result_i.grid(row=5, column=0, columnspan=2, pady=5)
result_r = tk.Label(root, text="")
result_r.grid(row=6, column=0, columnspan=2, pady=5)

root.grid_columnconfigure(1, weight=1)

root.mainloop()