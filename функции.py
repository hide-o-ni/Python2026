#меню с мат функциями
guest = '1'

def menu():
    print (" 'm' меню")
    print (" 'sq' площадь квадрата")
    print (" 'r' площадь прямоугольника")
    print (" 'с' площадь круга")
    print (" 'q' выход")

def S_sq (a):   #площадь квадрата
    print  ("площадь квадрата равна", float ( a*a))

def S_rect (a,b): #площадь прямоугольника
     print  ("площадь прямоугольника равна - ", float (a*b))     
    

def S_cir (a):  #площадь круга
    print  ("площадь квадрата равна - ", float (3.14 * a**2))
    
menu ()
while guest != 'q':
    guest = (input("ввод: "))
    
    if guest == 'm':
         menu()
    elif guest == 'sq':
        a = float (input ("введите значение стороны квадрата - "))
        S_sq (a)
    elif guest == 'r':
        print ("введите два значения - высоту и ширину прямоугольника: ")
        a = float (input ("длина - "))
        b = float (input ("ширина - "))
        S_rect (a, b)
    elif guest == 'c':
        a = float (input ("введите радиус круга - "))
        S_cir (a)
    

