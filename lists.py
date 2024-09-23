#  find sum and average
l= [1,2,3]
print("sum=",sum(l))
print("average=",sum(l)/len(l))


# reverse of list
l=[1,2,3]
l.reverse()
print(l)


# reverse the list using slicing
l= [1,2,3,4,45]
print(l[ ::-1])


# write a program to extract even and odd number from a given list
l =[]
n= int(input("enter the size of list"))
for i in range(n):
    ele= int(input())
    l.append(ele)
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even=",even)
print("odd=",odd)


# write a program to find the position of minimum and maximum element in the list
l=[]
n= int(input("enter the size of list"))
for i in range(n):
    ele= int(input("enter the elements"))
    l.append(ele)
print(l)
print("max=",max(l))
print("min=",min(l))


# interchange the first and last element in the list
l =[1,2,34,5,6]
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)


# write a program to remove first occurrence of a given element in the list
l= [1,2,3,1,5,1,2,]
l.remove(1)
print(l)


