#simple string and variable examples
x  =2
y = 3
if type(x) == type(y):
    print(type(x))
marks = 90, 78, 88
gopi, karthi, subin = marks
print("the marks obtained by gopi is", gopi)
print("the marks obtained by karthi is", karthi)
print("the marks obtained by subin is", subin)
firstname = "Gopi"
lastname = "nath"
fullname = firstname+lastname
print(fullname, marks)

breakfast = "poha"
def food():
    global breakfast
    breakfast="poha"
    print("\nmorn Breakfast:", breakfast)
food()
print("Lunch:", breakfast)
l="""i wakeup early in the morning, \"gopi\" go for a jog
i do some programming,
i eat , i go to office"""
print('\n',"the first letter of para is", l[0])
print("\n the length o string is", len(l))
print('\n', "office" in l)
print(l)

txt = "The best things in life are free! sometimes expensive"
if "expensive" in txt:

  print("yes, 'expensive' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
a = "Hello, World!"
print(a.upper())
x="   helloworld    "
print(x.upper())
print(x.split('l'))

x="sriniwas"
lastname="suryawanshi"
print(len(lastname))
fullname=x+lastname
age=24
print("My roomate name is",  fullname)
print(fullname.upper())
print(x+ " " + lastname)
details="his age is {}"
print(details.format(age))
print("his age is", age)
item="apple"
quantity=30
price=500
total="I want to pay {2} dollars for {0} pieces of item {1}"
print(total.format(quantity, item, price))

txt = "\107\117\120\111\116\101\124\110"
print(txt)
print(item.find(a))

#output
"""
<class 'int'>
the marks obtained by gopi is 90
the marks obtained by karthi is 78
the marks obtained by subin is 88
Gopinath (90, 78, 88)

morn Breakfast: poha
Lunch: poha

 the first letter of para is i

 the length o string is 96

 True
i wakeup early in the morning, "gopi" go for a jog
i do some programming,
i eat , i go to office
yes, 'expensive' is present.
No, 'expensive' is NOT present.
HELLO, WORLD!
   HELLOWORLD    
['   he', '', 'owor', 'd    ']
11
My roomate name is sriniwassuryawanshi
SRINIWASSURYAWANSHI
sriniwas suryawanshi
his age is 24
his age is 24
I want to pay 500 dollars for 30 pieces of item apple
GOPINATH
-1
"""
