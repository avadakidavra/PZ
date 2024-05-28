# в последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

from functools import reduce


def average_of_slice(sequence, slice_ratio):
    slice_size = len(sequence) * slice_ratio
    selected_slice = sequence[:int(slice_size)]
    total = reduce(lambda x, y: x + y, selected_slice)
    average = total / len(selected_slice)
    return average


sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = average_of_slice(sequence, 1 / 3)
print("Среднее арифметическое выбранной части:", result)
