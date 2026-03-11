def is_subsequence(s, t):
    list1 = list(s)
    list2 = list(t)
    flag = True            
    for i in list1:
        if i not in list2:
            flag = False 
            break 
    return flag

s = input().strip()
t = input().strip()
result = is_subsequence(s, t)
print(result)