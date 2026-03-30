def Recurcive_max (arr):
    #выполняется пока список не равен одному элементу
    if not arr:                  #начало блока
        return  0
        
    if len(arr) == 1:
        return arr[0]
        
    maxx = Recurcive_max (arr [1:])   #конец блока
    
   
    if arr[0] > maxx:             #потом это
       return arr[0]
    else:
        return maxx
    
    
arr = [2,3,1]
result = Recurcive_max (arr)
print (result)