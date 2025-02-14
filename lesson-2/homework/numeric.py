# 1
a = float(input('Enter a number: '))
print(round(a, 2))

# 2
a, b, c = int(input('Enter a number: ')), int(input('Enter a number: ')), int(input('Enter a number: '))
print("Largest number:", max(a,b,c),"Smallest number:", min(a,b,c))

#3
kilometers = float(input("Enter a kilometers: "))
print(kilometers*1000, "meters")
print(kilometers*100_000, "centimeters")

#4
a,b = int(input('Enter first number: ')),int(input('Enter second number: '))
print("Integer division is:", max(a,b)//min(a,b), "The remainder is:", max(a,b)%min(a,b))

#5
celcius = float(input("Temperature in Celcius: "))
fahrenheit = (9/5)*celcius+32
print(fahrenheit)

#6
number = int(input('Enter a number: '))
print("The last digit of the number is {}".format(number%10))

#7
num = int(input('Enter a number: '))
if (num%2 == 0):
    print('Even')
else:
    print('Odd')