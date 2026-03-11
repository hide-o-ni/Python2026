from collections import Counter

def find_unique_elements(list1, list2):
#    result = []            #не работает с одинаковыми значениями 
 #   for i in list1:
  #      if i not in list2:
   #         result.append(i)
    #return result   
    
    dict1 = Counter (list1)
    dict2 = Counter (list2)
    result = dict1 - dict2
    return  list(result.elements())

list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))
result = find_unique_elements(list1, list2)
print(' '.join(map(str, result)))