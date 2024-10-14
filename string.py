# reverse of string using slicing
n=input("enter the value")
print(n[::-1])


# reverse of string without using slicing
n=input("enter the value")
rev=""
for i in n:
    rev=i+rev
print(rev)



# check the given string is palindrome
n=input("enter the value")
rev=""
for i in n:
    rev=i+rev
if n==rev:
    print("palindrome")
else:
    print("not palindrome")


# print even length words in a string
n=input("enter the string").split()
for i in n:
    if len(i)%2==0:
        print(i)


# count the number of vowels in the string
n=input("enter the string")
print(n)
count=0
for i in n:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print(count)



# find length of the string without using len() function
str=input('enter the string')
count=0
for i in str:
    count=count+1
print(count)    
