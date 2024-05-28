#Дана строка "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4" Преоброзовать информацию из строки в словарь, найти среднее арифметическое оценок,результат вывести на экран
student = {}
inf = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
inf = inf.split()
student['Фамилия'] = inf[0]
student['Имя'] = inf[1]
student['Отчество'] = inf[2]
student['Группа'] = inf[3]
student['Оценки'] = []
for i in inf[3:]:
    student['Оценки'].append(int(i))
print(student)
lenStud = len(student['Оценки'])
lenStud2 = sum(student['Оценки'])
print('Средний бал')
print(lenStud2 / lenStud )