
# Создайте функцию для конвертации из Цельсия в Фаренгейт
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius*9/5 + 32
    return fahrenheit
     
# Чтение входных данных
temperature = float(input())
# Выполнение конвертации
result = celsius_to_fahrenheit(temperature)
# Вывод результата, округленного до двух знаков после запятой
print(f"{result:.2f}")
