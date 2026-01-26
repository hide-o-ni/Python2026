
'''
#продалжает запрашивать числа, пока не будет введено 0
#выводит среднее значение
count = 0
summa = 0.0
guest = 1

print ("введите 0 чтобы выйти")

while guest != 0:
    guest = float (input ("введите число"))
    if guest != 0:
        count = count +1
        summa = summa+guest
    if guest == 0:
        print ("среднее значение составило", summa / count)


#запрашивает имя пользователя и отвечает

print ("введите cat чтобы выйти")
name = 'l'
while name != 'cat':
    name  = input ("введите свое имя ")
    if name == 'Ваня':
     print("а кто это тут булочка? а это же Ваня!")
    elif name == 'Паша':
      print ("иди мыть посуду Паша")
    elif name == 'Оля':
     print ("иди учиться Оля")
    else:
     print ("у тебя красивое имя ", name)

#запрашивает 2 числа и если сумма 100, то выводит сообщение
sum = 100

print ('введите два числа')
guest1 = int (input ())
print ()
guest2 = int (input ())
print ()
if guest1 + guest2 == sum:
    print ("это большое число - ", guest1 + guest2)
else:
    print ("твое число - ",guest1 + guest2 )

'''


