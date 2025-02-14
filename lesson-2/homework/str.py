#1
name = input('Enter your name: ')
year_of_birth = int(input('Enter your year of birth: '))
print('Your age is', 2025 - year_of_birth)

#2
txt = 'LMaasleitbtui'
print(txt[1::2])
print(txt[0::2])
3
str = input('Enter a string: ')
print(len(str), str.lower(), str.upper())

#4
my_string = input("Enter a string: ")
reversed_string = my_string[::-1]
if reversed_string == my_string:
   print("The string is a palindrome")
else: print("The string is not a palindrome")

#5
str1 = input('Enter a string: ')
vowels = "aeiouAEIOU"
count_vowels = 0
count_consonants = 0
for i in range(len(str1)):
    if str1[i].isalpha() and str1[i] in vowels:
        count_vowels += 1
    elif str1[i].isalpha() and str1 not in vowels:
        count_consonants += 1
print("Number of vowels:", count_vowels, "\nconsonants:", count_consonants)

#6
str6_1 = input('Enter a string: ')
str6_2 = input('Enter another string: ')
if str6_2 in str6_1:
    print("The second string", str6_2, "is in the first string", str6_1)
else: print("it does not contain")

#7
str7_1 = input('Input sentence: ')
str7_2 = input('Replace: ')
str7_3 = input('With: ')
output = ''
list7 = str7_1.split()
for i in range(len(list7)):
    if list7[i]==str7_2:
        list7[i] = str7_3
        output += str7_3 + " "
    else:
        output += list7[i] + " "
print(output)

#8
str8 = input('Enter string: ')
print("The first char is", str8[0], "and the last char is", str8[-1])

#9
str9 = input('Enter string: ')
print(str9[::-1])

#10
sentence =input('Enter sentence: ')
print(len(sentence.split()))

#11
str11 = input('Enter a string: ')
digits = '1234567890'
count_digits = 0
for i in range(len(str11)):
   if str11[i] in digits:
       count_digits += 1
       print("String contains digit", (str11[i]))
if count_digits == 0:
   print("String does not contain digit")

#12
str12 = "Hello World! how are you? I am fine thank you"
print(str12.replace(" ","-"))

#13
str13 = input('Enter a string: ')
print(str13.replace(" ",''))


#14
str14_1 = input('Enter string: ')
str14_2 = input('Enter another string: ')
if str14_1 == str14_2: print("equal")
else : print("not equal")

#15
str15 = input('Enter a sentence: ')
list = str15.split()
for i in range(len(list)):
   print(list[i][0], end="")

#16
str16 = input('Enter a string: ')
char16 = input('Enter a character: ')
str16_1 = ''
for i in range(len(str16)):
   if str16[i] != char16:
       str16_1 += str16[i]
print(str16_1)

#17
str17 = input('Enter a string: ')
vowels = "aeiouAEIOU"
str17_1 = ''
for i in range(len(str17)):
   if str17[i] not in vowels:
       str17_1 += str17[i]
   else: str17_1 += str17[i].replace(str17[i], "*")
print(str17_1)

#18
str18 = input('Enter a string: ')
list18 = str18.split()
print("Starts with:", list18[0], "and ends with:", list18[-1])