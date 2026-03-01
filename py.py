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


#сравнение переменных

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print ("too low")
    if number == guess_me:
        print ("found it")
        break
    if number > guess_me:
        print ("oops")
        break
    number +=1

#сравнение переменных с циклом for

guess_me = 5

for number in range (10):
    if number < guess_me:
        print ("too low")
    elif number == guess_me:
        print ("found it")
        break
    else:
        print ("oops")
        break

#списки

#мой год рождения
year_list= [year for year in range (1994,2000)]
print (year_list)
print ("мне больше всего лет из списка",max(year_list)) 
print ("мне было 3: ", year_list[3])


#другое
things = ["mozzarella", "cinderella","salmonella"]
things [1] = things [1].capitalize ()
things [0] = things [0].upper ()
del things [2]
print (things)


#
surprice = ["Groucho", "Chico", "Harpo"]
surprice [-1] = surprice [-1].lower ()
surprice [-1] = surprice [-1] [::-1]
print (surprice [-1])

#
even =  [i for i in range (10) if i % 2 == 0]
print (even)


#кортеж
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
start1_caps = ' '.join([word.capitalize () + '!' for word in start1])
for first, second in rhymes:
    print (f"{start1_caps} {first.capitalize ()}!")
    print (f"{start2} {second}.")


#словари и множества
ef2 = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print (ef2.get ('walrus'))
f2e = {}
for en,fr in ef2.items():
    f2e [fr] = en
print (f2e)
#
print (f2e ['chien'])
#
set_list = []
for word in ef2.keys():
    set_list.append (word)
print (set_list)
#

#
life = {
        'animals': {
                 'cats' : [
                        'Henri', 'Grumpy', 'Lusy'
                            ],
                    'octopi':{},
                    'emus':{}
                    },
                    'plants':{},
                    'other':{}
        }

print (life)
print (f"высокоуровневые ключи {list (life.keys())} ")
print (life['animals'].keys())
print (life['animals']['cats'])

#
squares = {word: word **2 for word in range (10)}
print (squares)


#
odd = {word for word in range(10) if word % 2 != 0}

#
for i in range (10):
    print (f"Got {i}")
print('2')

for i in (('Got %s' %i) for i in range (10)):
    print (i)

'''

#
keys = ('optimist','pessimist', 'troll')
values =  ('the glass if half full', \
            'the glass if half empty', \
            'how did you get a glass?')
        
fzip = dict (zip (keys, values))          
print(fzip)

#
    
