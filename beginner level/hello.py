n=input('Enter the number')  
list = ['HELLO'] 
def func(x):
     print (x * int(n))
def simple(fun,list):
     for item in list:
         fun(item)
simple(func, list)
 
