# Дан целочисленный список размера N. Если он является перестановкой, то есть
# содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
# первого недопустимого элемента.
def check_permutation(lst):
    n = len(lst)
    visited = [False] * n

    for num in lst:
        if num < 1 or num > n or visited[num - 1]:
            return num
        visited[num - 1] = True

    return 0


input_list = [4, 1, 3, 2, 5]
result = check_permutation(input_list)
print(input_list)
print(result)
