def square (x):
    s =x**2
    return s
x = float(input("Длина стороны квадрата: "))
result = square(x)
import math
round_result = math.ceil(result)
print(f'Округление в большую сторону сумма-{round_result}')

