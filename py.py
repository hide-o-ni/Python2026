'''
# Чтение входных данных
score = int(input())

if score>=90 and score<=100:
    grade = "A"
elif score>=80 and score<=89:
    grade ="B"
elif score>=70 and score<=79:
    grade="C"
elif score>=60 and score<=69:
    grade ="D"
else:
    grade ="F"

# Вывод результата
print(grade)


########
# Считайте список чисел из одной строки
numbers = list(map(int, input().split()))

# Выведите первый элемент списка
print(numbers [0])

# Выведите последний элемент списка
print(numbers[-1])

########
# Выведите третий элемент списка (если он существует, иначе выведите "No third element")

print("No third element") if numbers[2] == None else print(numbers[2])

numbers = list(map(int, input().split()))

# Добавьте число 100 в конец списка
numbers.append(100)

# Удалите первый элемент из списка
#del numbers [0]
numbers.pop(0)
# Выведите измененный список в одну строку, с элементами, разделенными пробелами#
#print(" ".join(map(str, numbers)))
print(' '.join(map))

#########
# Функция для вычисления статистики и возврата в виде кортежа
def calculate_stats(a, b):
    summ = a+b
    product =a*b
    middle=float ((a+b)/2)
    return summ,product,middle

# Считываем ввод
a, b = map(int, input().split())

results = calculate_stats(a, b)
print(results[0])
print(results[1])
print(results[2])

'''

# Создайте функцию для поиска общих элементов между двумя списками
def find_common_elements(list1, list2):
    # Ваш код здесь
    pass

# Считываем два списка
list1 = input().split()
list2 = input().split()

# Находим и выводим общие элементы в алфавитном порядке
result = find_common_elements(list1, list2)
print(result)
