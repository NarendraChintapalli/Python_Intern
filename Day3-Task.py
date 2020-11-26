Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Merging two python dictionaries
>>> MobileDictionary1={1001:"Ipone",1002:"Vivo"}
>>> MobileDictionary2={1003:"Oneplus",1004:"Oppo"}
>>> MobileDictionary1
{1001: 'Ipone', 1002: 'Vivo'}
>>> MobileDictionary2
{1003: 'Oneplus', 1004: 'Oppo'}
>>> MobileDictionary1.update(MobileDictionary2)
>>> MobileDictionary1
{1001: 'Ipone', 1002: 'Vivo', 1003: 'Oneplus', 1004: 'Oppo'}
>>> dic1={1:"one",2:"two"}
>>> dic2={3:"three",4:"four"}
>>> dic3={**dic1,**dic2}
>>> dic3
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> 
>>> 
>>> 
>>> #Removing a key from Dictinary
>>> Customer_details={"cid":1111,"came":"prabhas","caddress":"mogalthur"}
>>> del Customer_details["cname"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del Customer_details["cname"]
KeyError: 'cname'
>>> del Customer_details["came"]
>>> Customer_details
{'cid': 1111, 'caddress': 'mogalthur'}
>>> del Customer details["caddress"]
SyntaxError: invalid syntax
>>> del Customer_details["caddress"]
>>> Customer_details
{'cid': 1111}
>>> students_dic={1001:"Ramya",1002:"Sowmya",1003:"Divya"}
>>> students_dic
{1001: 'Ramya', 1002: 'Sowmya', 1003: 'Divya'}
>>> del students_dic[1001]
>>> students_dic
{1002: 'Sowmya', 1003: 'Divya'}
>>> 
>>> 
>>> 
>>> #Mapping two lists into dictionary
>>> keys=["Ramya","Sowmya","Divya","Sai","Varma"]
>>> values=[100,101,102,103,104]
>>> d=dict(zip(keys,values))
>>> print(d)
{'Ramya': 100, 'Sowmya': 101, 'Divya': 102, 'Sai': 103, 'Varma': 104}
>>> 
>>> 
>>> 
>>> #Finding the length of a set
>>> a={"Ramya","Sowmya","Divya","Sai","Varma"}
>>> a
{'Sowmya', 'Varma', 'Ramya', 'Sai', 'Divya'}
>>> len(a)
5
>>> b={10,20,30,40,50}
>>> b
{50, 20, 40, 10, 30}
>>> len(b)
5
>>> c={"Iphone","Oneplus","Vivo","Realme"}
>>> len(c)
4
>>> 
>>> 
>>> 
>>> #Removing the intersection of 2nd set from the 1st set
>>> set1={100,200,300,400,500,600,700,800}
>>> set2={100,200,300,400,500,900}
>>> set3=set1.intersection(set2)
>>> set3
{100, 200, 300, 400, 500}
>>> set3.remove(500)
>>> set3
{100, 200, 300, 400}
>>> set3.remove(400)
>>> set3
{100, 200, 300}
>>> set3.remove(300)
>>> set3
{100, 200}
>>> set3.remove(200)
>>> set3
{100}
>>> set3.remove(100)
>>> set3
set()
>>> 