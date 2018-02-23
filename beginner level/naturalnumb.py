numb=int(input("Enter the number"))
if numb < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(numb > 0):
       sum += numb
       numb -= 1
   print("The sum is",sum)
