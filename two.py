import sys

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

def square(x):
    return x*x

class Point():
    def __init__(self,input1,input2):
        self.x=input1
        self.y=input2
p=Point(1,2)
print(p.x)
print(p.y)
class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passengers)
flight=Flight(3)
for name in names:
    if flight.add_passenger(name):
        print(f"Added {name} to flight successfully.")
    else:
        print(f"No available seats for {name}.")

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("Hello, world!")
hello()
people=[
    {"name":"Harry","gender":"Male"},
    {"name":"Ron","gender":"Male"},
    {"name":"Hermione","gender":"Female"}
]
people.sort(key=lambda person: person["name"])
print(people)

try:
    p=int(input("p: "))
    q=int(input("q: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)
try:
   result=p/q
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
print(f"{p}/{q}={result}")