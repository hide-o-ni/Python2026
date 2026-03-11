def reverse_letters(input_string):
    list1 = input_string. split()
    list2 = []
    for i in list1:
        list2.append(i [::-1])
    
    return ' '.join (list2)
        
        

input_string = input().strip()
print(reverse_letters(input_string))
