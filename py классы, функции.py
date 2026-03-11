def summ_element (arr):
    summ = 0
    for i in arr:
        sum += i
    return summ 
    
    
    # 1 2 3
    
def summ_element_R (arr): 
    if not arr:
        return  0 
         
    return arr[0] + summ_element_R (arr [1:])

arr = [1,3,1]
result = summ_element_R (arr)
print (result)


#
def good ():
    my_list =  ['Harry','Ron','Hermione']
    return my_list

result = good ()
print (result)


#создает генератор нечетных и возвращает 3 значение
def get_odds ():
    for number in range (1,10,2):
        yield number

def get_oddss ():
    elements = (i for i in range (10) if i%2!=0) # 1 вариант  
    count = 0
    for elem in elements:
        count +=1
        if count ==3:
            print (elem)

count = 1
for number in get_odds():                          # 2 вариант
    if  count == 3:
        print ('3 число  - ')
        break
    count +=1

        
#result = get_odds ()
print (get_oddss ())


# то же самое с декоратором
def test (func):
    def get_oddss():
        print ('start')
        result = func ()
        print ('end')
    return get_oddss
        
@test
def get_oddss ():
    elements = (i for i in range (10) if i%2!=0)
    count = 0
    for elem in elements:
        count +=1
        if count ==3:
            print (elem)
        

#result = get_odds ()
print (get_oddss ())

#
class OopsException (Exception ):
    pass


try:
    raise OopsException ('Caught an oops')
except OopsException as ex:
    print (ex)
    
list1 = [1,2,3]
for i in range(len(list1)):
    if i ==2:
        raise OopsException ('Caught an oops')
        


#классы
class Thing ():
    pass 

obj = Thing ()
print (obj)
print (Thing)

#
class Thing2:
    letters = 'abc'
    
    
print (Thing2.letters) 


class Thing3:
    def __init__ (self):
        self.letters = 'xyz'
    
    
print (Thing3.letters) 
obj = Thing3 ()
print (obj.letters)

#
class Element ():
    def __init__ (self, name,  symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
    

elem = Element ('Hydrogen', 'H', 1)    
print (elem) 

#
class Element ():
    def __init__ (self, name,  symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
d = {'name': 'Hydrogen', 'symbol' :'H', 'number' :  1}    
hydrogen = Element (**d)

print (hydrogen.name, hydrogen.symbol, hydrogen.number) 

#
class Element ():
    def __init__ (self, name,  symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump (self):
        print (self.name, self.symbol, self.number )
    
  
hydrogen = Element ('Hydrogen', 'H', 1)   
hydrogen.dump ()

#
class Element ():
    def __init__ (self, name,  symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__ (self):
        return  ('name = %s, symbol = %s, number = %s'%(self.name, self.symbol, self.number ))
    
  
hydrogen = Element ('Hydrogen', 'H', 1)   
print (hydrogen)

#
class Element:
    def __init__ (self, name,  symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property 
    def get_name (self):
        return  self.__name
        
    @property
    def get_symbol (self):
        return   self.__symbol 
        
    @property
    def get_number (self ):
        return   self.__number 
    
    
hydrogen = Element ('Hydrogen', 'H', 1)   
print (hydrogen.get_name)
print (hydrogen.get_symbol)
print (hydrogen.get_number)



#
class Bear:
    def eats ():
        return 'berries'

class Rabbit:
    def eats ():
        return 'clover' 

class Octothorpe:
    def eats ():
        return 'campers' 
        
bear = Bear
rabbit  = Rabbit
octothorpe = Octothorpe
print ('bear eats - ', bear.eats())
print ('rabbit eats - ', rabbit.eats())
print ('octothorpe eats - ', octothorpe.eats())

#
class Lazer:
    def does (self):
        return '--disintegrate--'

class Claw:
    def does (self):
        return 'crush' 

class SmartPhone:
    def does (self):
        return 'ring' 
class Robot:
    def __init__ (self):
        self.lazer = Lazer ()  
        self.claw = Claw ()
        self.smartphone = SmartPhone ()
    def does (self):
        print ('--работает робот--')
        print (self.lazer.does(),self.claw.does(), self.smartphone.does() )
        
l = Lazer()   
print (l.does())
r = Robot ()
print (r.does())




           