'''
#добавление числа к сумме
a=1
s=0
print ('введите числа для добавления к сумме')
print ('введиет 0 для выхода')
while a != 0: #0 - это выход из цикла
    print ('сумма  - ', s)
    a = float (input ('введите число: '))
    s=s+a
print ('текущая сумма равна', s)


#последовательность фибоначчи
a=0
b=1
count =0
maxcount = 20
#как только цикл запущен мы остаемся в нем
while count < maxcount:
    count+=1
    olda = a
    a=a+b
    b=olda
    print (olda, end=" ")
print ()
'''

#логин и пароль
print ('авторизуйтесь в системе')
login = input ('логин - ')
print ('введите пароль ')
pass_1 = input ('пароль - ')
print ('повторите пароль - ')
pass_2 = input ('пароль - ')
while pass_1 !=pass_2:
    print ('второй раз пароль введен неверно, введите заново  ')
    pass_2 = input ()
print ('вы авторизованы успешно')
print ('чтобы заблокировать компьютер введите lock')
command = None
pass_0 = None
log_0 = None
while command != 'lock':
    command = input ('одну команду верно написать не можешь - ')
while log_0 !=login:
    log_0 = input ('давай вспоминай логин - ')
while pass_0 != pass_1:
    pass_0 = input ('да хотя бы пароль напиши верно - ')
print ('не обольщайся')    
    
