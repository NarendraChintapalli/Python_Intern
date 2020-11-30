#List of numbers
number=[10,12,11,20,25]
print(number)
number=[i+2 for i in number]
print("The added list is:",number)



#Pattern Program
x=5
for i in range(0,x+1):
    for j in range(x-i,0,-1):
        print(j,end=' ')
    print()
    


#Fibonacci sequence
a=0
b=1
n=int(inter("ENTER THE NUMBER OF FIBONACCI SERIES GENERATED:"))
if n<=0:
    print("NOT POSSIBLE")
elif n==1:
    print(a)
elif n>=2:
    print("{},{}".format(a,b),end=' ')
for i in range(2,n):
    c=a+b
    print(",{}".format(c),end=' ')
    a=b
    b=c
    

#Armstrong number
num=int(input("enter the number:"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num=sum:
    print(num,"is a Armstrong Number")
else:
    print(num,"is not a Armstrong Number")
    
    

#Multiplication table of 9
for i in range(1,21):
    print(i,'*',9,'=',i*9)



#Checking the number is positive or negative
Number=int(input("please enter your number:"))
if Number==0:
    print(Number,"is 0")
elif Number>0:
    print(Number,"is positive")
else:
    print(Number,"is Negative")
    


#Converting the number of days to ages
days=int(input("please enter number of days:"))
years=int(days/365)
weeks=int(days%365)/7
print("The Age for",days,"days is",years,"years,"years and",weeks,"weeks.")



#Trignometry problem using MATH function
import math
sum_number=math.cos(math.pi/6)+math.sin(math.pi/6)
print("The sum of cos(pi/6) and sin(pi/6) is",sum_number)



#CALICULATOR program using if condition
print("CALICULATOR")
operation=int(input("please enter your choice:"))

if operation == 1:
    a=int(input("please enter first number:"))
    b=int(input("please enter seconf number:"))
    print("ADDITION OF TWO NUMBERS",a,"AND",b,"IS",a+b)
elif operation == 2:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("SUBTRACTION OF TWO NUMBERS",a,"AND",b,"IS",a-b)
elif operation == 3:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("MULTIPLICATION OF TWO NUMBERS",a,"AND",b,"IS",a*b)
elif operation ==4:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("DIVISION OF TWO NUMBERS",a,"AND",b,"IS",a/b)
else:
    print("please make valid choice from 1 to 4")
 
    
    

    
    
    
