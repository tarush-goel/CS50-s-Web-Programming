"""
print("Hello, world!")
a,b,c,d,e = 28,1.5,"Hello",True,None
name=input("Name: ")
print("Hello, "+name)
print(f"Hello, {name}")
n=int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
myname="Tarush"
print(myname[1])
names=["Harry","Ron","Hermione"] #list
print(names[1])
names.append("Ginny")
names.sort()
print(names)
x,y=10.0,20.0 #tuple
coordinate=(x,y)
s=set() #set
s.add(2)
s.add(1)
s.add(3)
print(s)
s.add(1)
print(s)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")
for i in range(6):
    print(i)
for name in names:
    print(name)
for character in myname:
    print(character)
gender={"Harry":"Male","Ron":"Male","Hermione":"Female"} #dictionary
gender["Ginny"]="Female"
print(gender["Harry"])
print(gender["Ginny"])
"""
def square(x):
    return x*x
class Point():
    def __init__(self,input1,input2):
        self.x=input1
        self.y=input2
p=Point(1,2)
print(p.x)
print(p.y)

