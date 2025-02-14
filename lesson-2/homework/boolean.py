#1
username = input("Enter your username: ")
password = input("Enter your password: ")
check1 = False
check2 = False
if username:
    check1 = True
else:
    print("Empty username")
if password:
    check2 = True
else: print("Empty password")

if not check1 and not check2:
    print("Unsuccessful login")

#2
n2 = int(input('Enter a number: '))
n2_1 = int(input('Enter another number: '))
check = True
if n2 == n2_1:
    check = True
else: check = False
if check:
    print("Equal")
else: print("Not equal")

#3
n3 = int(input('Enter a number: '))
if (n3 > 0 and n3%2==0):
    print('It is positive and even')
else: print('It is not')

#4
n4_1 = int(input('Enter a number: '))
n4_2 = int(input('Enter a number: '))
n4_3 = int(input('Enter a number: '))
if ( n4_1 == n4_2 or n4_1 == n4_3 or n4_2 == n4_3):
    print("All of them are not different")
else: print("All of them are different")

#5
str5 = input("Enter a string: ")
str5_1 = input("Enter a string: ")
if (len(str5) == len(str5_1)):
    print("They have the same length")
else: print("They have different lengths")

#6
n6 = int(input('Enter a number: '))
if (n6%3 == 0):
    if (n6%5 == 0):
        print(n6, 'is divisible by both 3 and 5')
    else: print(n6, 'is only divisible by 3')
elif (n6%5 == 0):
    print(n6, 'is only divisible by 5')
else: print(n6, 'is not divisible by both 3 and 5')

#7
n7_1 = float(input('Enter a number: '))
n7_2 = float(input('Enter a number: '))
if (n7_1 + n7_2) > 50.8:
    print('Sum is greater than 50.8')
else: print('Sum is not greater than 50.8')

#8
n8 = int(input('Enter a number: '))
if (10 <= n8 and n8 <= 20):
    print('It is between 10 and 20')
else: print('It is not between 10 and 20')