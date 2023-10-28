#Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
def isleapyear(year):
  if(year%4==0):
    print ("it is leap year ")
  else:
    print ("it is not a leap year ")
num=int(input ("enter the year "))
res=isleapyear(num)
