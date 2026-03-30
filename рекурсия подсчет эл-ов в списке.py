def Recurcive_count (arr):
    if not arr:
        return  0 
    
    
    return 1   + Recurcive_count (arr [1:])


arr = [1,3,1]
result = Recurcive_count (arr)
print (result)