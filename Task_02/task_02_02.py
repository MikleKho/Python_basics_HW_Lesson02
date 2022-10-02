# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]
n = int(input("Введите число ---> "))
if n >= 1:
    step = 1
elif n <= -1:
    step = -1
else:
    print("Input error")
    exit()
start = step
result = 1
print("Факториалы чисел: ")
for i in range(step, n + step, step):
    result = result * i
    print(f" {result}")
