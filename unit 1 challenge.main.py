
#Implement a recursive function to calculate the factorial of a given number.
def factorial_recursion(n):
  if(n==0 |n==1):
     return 1
  else:
    return n*factorial_recursion(n-1)
num=int(input("enter the value:"))
res=factorial_recursion(num)
print ("the factorial of {} is{}". format (num,res))