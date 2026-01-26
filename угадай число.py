
'''
n = int (input ("число ?"))
if n<0:
    print ("абсолютное значение", n, "равно", -n )
else:
    print ("абсолютное значение", n, "равно", n)
'''
#угадайка
number = 16
guess = -1
count = 0

print ("угадай число!")
while guess!= number:
    guess = int(input("и твое числооо...."))
    count = count + 1
    if guess == number:
        print ("угадал!")
    elif guess < number:
        print ("это число больше")
    elif guess > number:
        print ("не такое большое")
    
    
if count > 3:
    print ("должно быть это было сложно")
else:
    print ("хорошая работа")
