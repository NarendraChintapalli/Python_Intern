Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Adding a item into the list
>>> Employee_departements=["IT","Accounting","Marketing","Finance"]
>>> Employee_departements
['IT', 'Accounting', 'Marketing', 'Finance']
>>> Employee_departements.append("HR")
>>> Employee_departements
['IT', 'Accounting', 'Marketing', 'Finance', 'HR']
>>> 
>>> 
>>> 
>>> #Removing an item in the list
>>> Employee_departements.remove("HR")
>>> Employee_departements
['IT', 'Accounting', 'Marketing', 'Finance']
>>> Employee_departements.remove("Finance")
>>> Employee_departements
['IT', 'Accounting', 'Marketing']
>>> Employee_departements.remove("Accounting")
>>> Employee_departements
['IT', 'Marketing']
>>> Employee_departements.remove("Marketing")
>>> Employee_departements
['IT']
>>> 
>>> 
>>> 
>>> #Creating a tuple and printing the reverse of the created tuple
>>> Tuple1=
SyntaxError: invalid syntax
>>> Tuple1=910,20,30,40,50,60)
SyntaxError: unmatched ')'
>>> Tuple1=(10,20,30,40,50,60)
>>> list1=list(Tuple1)
>>> list1
[10, 20, 30, 40, 50, 60]
>>> list1.reverse()
>>> list1
[60, 50, 40, 30, 20, 10]
>>> Tuple1=("Rmya","Sowmya","Divya")
>>> list1.reverse()
>>> list1
[10, 20, 30, 40, 50, 60]
>>> Tuple1=("Ramya","Sowmya","Divya")
>>> list1=list(Tuple1)
>>> list1
['Ramya', 'Sowmya', 'Divya']
>>> list1.reverse()
>>> list1
['Divya', 'Sowmya', 'Ramya']
>>> 
>>> 
>>> 
>>> #Creating a tuple and Converting tuple into list
>>> Tuple1=("Employeeid","Employeename","Employeeaddress","Employee phonenumber")
>>> list1=list(Tuple1)
>>> list1
['Employeeid', 'Employeename', 'Employeeaddress', 'Employee phonenumber']
>>> Tuple1=(10,11,22,33,44,55,66,777)
>>> list1=list(Tuple1)
>>> list1
[10, 11, 22, 33, 44, 55, 66, 777]
>>> 