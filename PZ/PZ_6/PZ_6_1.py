# Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех элементов списка, кроме элементов с номером
# от K до L включительно.
def find_sum_except_range(numbers, k, l):
    if k >= l or l >= len(numbers):
        return "Некорректные значения K и L"

    sum_except_range = 0
    for i in range(len(numbers)):
        if i < k or i > l:
            sum_except_range += numbers[i]

    return sum_except_range


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
k = int(input("Значение K: "))
l = int(input("Значение L: "))
result = find_sum_except_range(numbers, k, l)
print(result)
