# Описать функцию Powerl(A, B) вещественного типа, находящую величину AB по формуле AB = exp(B*ln(A)) (параметры A и B -
# вещественные.) В случае нулевого или отрицательного параметра A функция возвращает 0. С помощью этой функции найти
# степени  A**P, B**P, C**P, если даны числа P, A, B, C.
import math

def Powerl(A, B):
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))

def calculate_powers(P, A, B, C):
    power_A = Powerl(A, P)
    power_B = Powerl(B, P)
    power_C = Powerl(C, P)
    return power_A, power_B, power_C


P = int(input("Ввести значение P: "))
A = int(input("Ввести значение A: "))
B = int(input("Ввести значение B: "))
C = int(input("Ввести значение C: "))

power_A, power_B, power_C = calculate_powers(P, A, B, C)

print(f"A в степени P: {power_A}")
print(f"B в степени P: {power_B}")
print(f"C в степени P: {power_C}")