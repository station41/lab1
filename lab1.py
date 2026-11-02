import math

alpha = float(input("Введите значение alpha: "))

# z1
num1 = math.sin(4 * alpha)
den1 = 1 + math.cos(4 * alpha)
num2 = math.cos(2 * alpha)
den2 = 1 + math.cos(2 * alpha)

z1 = (num1 / den1) * (num2 / den2)

# z2
ugol = (3 * math.pi / 2) - alpha
z2 = math.cos(ugol) / math.sin(ugol)

print(f"Результат z1 = {round(z1, 4)}")
print(f"Результат z2 = {round(z2, 4)}")