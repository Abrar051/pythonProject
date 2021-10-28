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


greet_user('abrar', 'shahriar')'''
