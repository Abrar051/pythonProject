('''First = input(" Enter first number : ")
Second = input(" Enter second number : ")
sum = float(First)+float(Second)
print(sum)
print(First+Second)

course = "Python learning"
course.upper()
print(course.upper())
print(course.find('learn'))
print(course.replace('learn','for'))
print(course.find('le'))

price = 25
print(price > 10 and price < 30)
print(not price>100)''')

('''if else statement''')

('''temperature=35

if temperature>30:
    print("It's a hot day")
elif temperature==30:
    print('Moderate temperature')
else:
    print("Cold day")

Weight=input("Enter your weight : ")
Option = input(" (K)g or (L)bs : ")
if Option.upper()=="K":
    print("Do it")
elif Option.upper()=="L":
    print("Do that")


i=1
while i<=5:
    print(i*'*')
    i=i+1

names = ["john","bob","mosh","mary"]
print(names)
print(names[0])
print (names[0:3])


numbers=[1,3,2,5,4]
numbers.insert(6,0)
print(numbers)
numbers.append(6)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.reverse()
print(numbers)
print(1 in numbers)

numbers=[1,2,3,4,5]
for item in numbers:
    print(item)

i=0
while i<len(numbers):
    print(numbers[i])
    i=i+1 ''')

('for loop')

('''for number in range(5,10,2):
    print(number)''')

('''tuples''')

('''numbers =(1,2,3)
numbers.count()''')

('''numpy
    pandas
    matplotlib
    scikit-learn
''')

'''print(bin(int(4)))

phone = input("Phone : ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output= ""
for ch in phone:
    output+=digits_mapping.get(ch,"!")+ " "
print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)":"happy face",
    ":(":"sad face"
}
output=""

for word in words:
    emojis.get(word,word)
    print(emojis.get(word,word))
    output=output+emojis.get(word,word)+ " "
print(output)


def greet_user():
    print('something')
    print('Abroad')


greet_user()


def greet_user(first_name):
    print(f'Hi {first_name}!')


greet_user("Abrar")


def greet_user(first_name, last_name):
    print(f'Hello {first_name} and {last_name} welcome')


greet_user('abrar', 'shahriar')


def square(number):
    return number * number


print(square(2))


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "happy face",
        ":(": "sad face"
    }
    output = ""

    for word in words:
        emojis.get(word, word)
        print(emojis.get(word, word))
        output = output + emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))'''

'''in java it is called try catch
try:
    age=int(input('Age : '))
    print(age)
except ZeroDivisionError:
    print('Age cannot be divided by zero')
except ValueError:
    print('Invalid input')'''

# this is how we can do comment in python

# now about class the most important part of python

numbers = [1, 2, 3, 4, 5, 6]

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 10
point2.y = 20
print(point2.x)

point = Point(10, 20)
point.x = 10
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


john = Person("John wick")
print(john.name)
john.talk()

bob = Person("Bob")
print(bob.name)
bob.talk()


class Mamal:
    @staticmethod
    def walk():
        print('walk')


class Dog(Mamal):
    @staticmethod
    def bark():
        print("bark")


class Cat(Mamal):
    @staticmethod
    def be_annoying():
        print("")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()'''
# importing items from another python file
'''
import converter
from converter import kg_to_lbs
from converter import find_max'''

'''kg_to_lbs(100)
print(converter.lbs_to_kg(50))
print(converter.kg_to_lbs(60))

for i in range(0, 5):
    print(i)
    i = i + 0.5

print(find_max([1, 2, 3, 6, 8]))'''

# package in python

'''import ecommerce.shipping
from ecommerce import shipping
from ecommerce.shipping import calc_shipping


shipping.calc_shipping()'''

'''import random

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']

leader = random.choice(members)
print(leader)'''

'''make a class which will contain a random function which we can call later for dice roll'''

'''import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())'''

# Absolute path
# Relative path

# for windows c:\Program Files\Microsoft
# /usr/local/bin

# Relative path

'''path = Path("ecommerce")
print(path.exists())
path = Path("emails")
print(path.mkdir())
path1 = Path()
print(path1.glob('*.py'))

from pathlib import Path

path = Path()

for file in path.glob('*.py'):
    print(file)

for file in path.glob('*'):
    print(file)'''

def add (a,b):
    return a+b

print(add(2,3))
