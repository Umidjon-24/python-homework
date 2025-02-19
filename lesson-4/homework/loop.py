#Question 1
def uncommon(list1, list2):
    count = 0
    result_list = list()
    for i in list1:
        if i not in list2:
            result_list.append(i)
    for x in list2:
        if x not in list1:
            result_list.append(x)
    return result_list
list1 = [1,2,3,1]
list2 = [2,3,4]
print(uncommon(list1, list2))

#Question 2
def square(n):
    for i in range (1,n):
        print(i**2)
n = 5    
square(n)

#Question 3
txt = input("Enter a string: ")
list3 = list()
vowels = ['a','e','u','i','o','A','E','U','I','O']
text = list()
lenth = len(txt)
a = 2
for i in range (len(txt)):
    if i == a:
        text.append(txt[i])
        if txt[i] not in vowels and i != len(txt)-1:

            text.append("_")
            vowels.append(txt[i])
            a += 3
            print(txt[i], 'worked', a)
        else: a+=1
    else:
        text.append(txt[i])
        print(txt[i])
        
print("".join(text))

#Question 4
import random
b = True
def guess(a):
    global b
    for i in range (10):
        n = int(input("Enter a number: "))
        if a == n:
            b = False
            print("Right!")
            break
        elif a>n:
            print("Too low")
            b = True
        else: 
            print("Too high")
            b = True

a = random.randint(1,100)
guess(a)
while b == True:
    print("Try again?")
    n = input()
    if n in ['yes']:
        guess(a)
        if b == False:
            break
    else:
        print("Stopped")
        b = False

#Question 5
def password(p):
    count_uppercase = 0
    for char in p:
        if char.isupper() == True:
            count_uppercase += 1 
    
    if len(p) < 8:
        print("Password is too short")
    elif count_uppercase == 0:
        print ("Password must contain an uppercase letter")
    else:
        print ("Password is strong")
        
p = input("Enter a password: ")
password(p)

#Question 6
for i in range (2,100):
    count = 0
    for x in range(1,i+1):
        if i%x == 0:
            count+=1
    if count <= 2:
        print(i)
        count = 0

#Bonus challenge
import random
point1 = 0
point2 = 0
while point1 < 5 and point2 < 5:
    user = input("Enter your choice (rock, paper, scissors): ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    if comp == user:
        print("Draw")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    if comp == 'rock' and user == 'paper':
        point1+=1
        print("+1 point for you")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    elif comp == 'rock' and user == 'scissors':
        point2+=1
        print("+1 point for computer")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    elif comp == 'paper' and user == 'scissors':
        point1+=1
        print("+1 point for you")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    elif comp == 'paper' and user == 'rock':
        point2+=1
        print("+1 point for computer")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    elif comp == 'scissors' and user == 'rock':
        point1+=1
        print("+1 point for you")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
    elif comp == 'scissors' and user == 'paper':
        point2+=1
        print("+1 point for computer")
        print("Comp has", point2, 'points')
        print('You have', point1, 'points')
if point1 == 5:
    print("You won!...:)")
else:
    print("You lost...:(")