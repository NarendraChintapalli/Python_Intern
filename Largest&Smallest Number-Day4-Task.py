#storing the Largest number from the list to a variable
a=[]
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter elements:"))
    a.append(b)
print(a)
Largest_number=max(a)
print(Largest_number)


#Storing the Smallest number from the list to a variable
a=[]
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter elements:"))
    a.append(b)
print(a)
Smallest_number=min(a)
print(Smallest_number)

