#угадай число, рекурсия к бинарному поиску
def Recursive_max (start, end, number,attempt = 1):  # 1- 100, 75
    if start == end:
        return attempt  #как минимум один раз программа отработает
    
    half = (start+end)//2 #определили половину - 50
    
    if half == number:   #50
        return attempt
    
    elif number > half:
        return Recursive_max (half +1, end, number, attempt+1) #51 -100
        
    
    else:
        return Recursive_max (start, half-1, number, attempt +1) #1-49
        
    
    
    
number = int(input("Загадайте число от 1 до 100: "))
if number >= 1 and number <= 100:
    print (Recursive_max (1, 100, number))