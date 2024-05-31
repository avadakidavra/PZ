#Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random

rows_matrix = int(input('Введите количество строк матрицы: '))
matrix = [([random.randint(-4, 2) for i in range(rows_matrix)]) for i in range(rows_matrix)]
flag = False

print('\nИсходная матрица:')
for i in range(len(matrix)):
 print(matrix[i])

for i in matrix:
 for j in i:
  if j > 0:
   flag = True

f= any(j>0 for j in i for i in matrix)
print(f'Результат: {f}')