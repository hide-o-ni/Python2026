'''# Создание комплексных чисел
z1 = 3 + 4j
z2 = complex(2, -3)  # 2 - 3j

# Получение действительной и мнимой частей
real_part = z1.real  # 3.0
imag_part = z1.imag  # 4.0

print (real_part)
print (imag_part)

real_part2 = z2.real  # 3.0
imag_part2= z2.imag  # 4.0

print (real_part2)
print (imag_part2)

#
a, b = map(int, input().split())


print('результат целочисленного деления', a//b)
print('результат обычного деления', a/b)

#
import math

# Чтение входных данных
a, b, c = input().split()
a = float(a)  # значение с плавающей точкой
b = int(b)    # целое число
c = float(c)  # число с плавающей точкой

round_a = round(a,2)
sqrt_b = math.sqrt(b)
floor_c = math.floor(c)

print('округление до 2 десятичных знаков')
print('квадратный корень')
print('округление вниз')

print(round_a)
print(sqrt_b)
print(floor_c)

#
# Считайте три логических значения
has_ticket = input() == "True" #ввод True
has_money = input() == "True" #ввод False
is_discount_day = input() == "True" #ввод True

result = has_ticket or (has_money and is_discount_day)
# Выведите результат (True или False)
print(result)




