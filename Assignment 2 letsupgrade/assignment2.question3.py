#Write a Python Program to find all occurrences of a character in the given string –
#program
str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")
i = 0

while(i < len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)
    i = i + 1