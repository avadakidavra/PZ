import tkinter as tk
from tkinter import ttk

root = tk.Tk()
title_label = tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(root, text="Ваше имя:")
name_label.grid(row=1, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")


password_label = tk.Label(root, text="Пароль:")
password_label.grid(row=2, column=0, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")


age_label = tk.Label(root, text="Возраст:")
age_label.grid(row=3, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")


gender_label = tk.Label(root, text="Пол:")
gender_label.grid(row=4, column=0, sticky="e")
gender_frame = tk.Frame(root)
gender_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")
male_radio = tk.Radiobutton(gender_frame, text="Мужской", value="male")
male_radio.pack(side="left")
female_radio = tk.Radiobutton(gender_frame, text="Женский", value="female")
female_radio.pack(side="left")

hobbies_label = tk.Label(root, text="Ваши увлечения:")
hobbies_label.grid(row=5, column=0, sticky="e")
hobbies_frame = tk.Frame(root)
hobbies_frame.grid(row=5, column=1, padx=10, pady=5, sticky="w")
music_check = tk.Checkbutton(hobbies_frame, text="Музыка")
music_check.pack(side="left")
video_check = tk.Checkbutton(hobbies_frame, text="Видео")
video_check.pack(side="left")
drawing_check = tk.Checkbutton(hobbies_frame, text="Рисование")
drawing_check.pack(side="left")


country_label = tk.Label(root, text="Ваша страна:")
country_label.grid(row=6, column=0, sticky="e")
country_combobox = ttk.Combobox(root, values=["Россия", "США", "Канада"])
country_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="we")

city_label = tk.Label(root, text="Ваш город:")
city_label.grid(row=7, column=0, sticky="e")
city_combobox = ttk.Combobox(root)
city_combobox.grid(row=7, column=1, padx=10, pady=5, sticky="we")

about_label = tk.Label(root, text="Кратко о себе:")
about_label.grid(row=8, column=0, sticky="ne")
about_text = tk.Text(root, height=3, width=20)
about_text.grid(row=8, column=1, padx=10, pady=5, sticky="we")


example_result_label = tk.Label(root, text="Решите пример, запишите результат в поле ниже:")
example_result_label.grid(row=9, column=0, columnspan=2, pady=5)
example_entry = tk.Entry(root)
example_entry.grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky="we")


cancel_button = tk.Button(root, text="Отменить ввод")
cancel_button.grid(row=11, column=0, padx=10, pady=10, sticky="e")
submit_button = tk.Button(root, text="Данные подтверждаю")
submit_button.grid(row=11, column=1, padx=10, pady=10, sticky="w")


root.grid_columnconfigure(1, weight=1)

root.mainloop()
