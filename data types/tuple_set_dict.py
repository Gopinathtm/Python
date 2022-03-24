#tuple, set, Dict Practise program
y = (34, 45, 32, 67, 45, 54, 23, 17)
x = (23,22,43)
z = x + y
print(z)
print()
print(y[-4:-1])
print(y[:4])

print()
y+= x
print(y)
if 34 in y:
    print("34 is in Y")
y = (34, 45, 32, 67, 45, 54, 23, 17)
x = list(y)
x[1] = 21
y = tuple(x)
print(y)
print()
fruits = ("apple", "orange", "banana", "potato", "lemon", "brinjal")
(*green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
for x in fruits:
    print(x)

for i in range(len(fruits)):
  print(fruits[i])

fruits = ("apple", "banana", "cherry")
mytuple = ("a", "b", "c")
addtuple = fruits + mytuple
print(addtuple)
y=x.count("22")
print(y)

n = {1,2,3,4,5,6,8,9}

print(len(n))
print(4 in n)

thisdict =  {
    "Brand": "ford",
    "model": "endevor",
    "number": "2342",
}
print(thisdict)
print(thisdict["Brand"])
print(len(thisdict))
x = thisdict.keys()
print(x)

thisdict ["color"] = "red"

print(thisdict)
y = thisdict.items()
thisdict["number"]  = 2020
print()
print(y)

thisdict ["number"] =  3950
thisdict.update({"Brand":"Volvo"})
print(thisdict)

for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
print()

for x,y in thisdict.items():
    print(x,y)

#output
"""
(23, 22, 43, 34, 45, 32, 67, 45, 54, 23, 17)

(45, 54, 23)
(34, 45, 32, 67)

(34, 45, 32, 67, 45, 54, 23, 17, 23, 22, 43)
34 is in Y
(34, 21, 32, 67, 45, 54, 23, 17)

['apple', 'orange', 'banana', 'potato']
lemon
brinjal
apple
orange
banana
potato
lemon
brinjal
apple
orange
banana
potato
lemon
brinjal
('apple', 'banana', 'cherry', 'a', 'b', 'c')
0
8
True
{'Brand': 'ford', 'model': 'endevor', 'number': '2342'}
ford
3
dict_keys(['Brand', 'model', 'number'])
{'Brand': 'ford', 'model': 'endevor', 'number': '2342', 'color': 'red'}

dict_items([('Brand', 'ford'), ('model', 'endevor'), ('number', 2020), ('color', 'red')])
{'Brand': 'Volvo', 'model': 'endevor', 'number': 3950, 'color': 'red'}
Volvo
endevor
3950
red
Brand
model
number
color

Brand Volvo
model endevor
number 3950
color red
"""


