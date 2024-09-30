tuple operations

# concatenation
t1=(1,2,3,4)
t2=(3,4,5)
print(t1+t2)

# repetition
t=(1,2,3,4,5)
print(t*3)


# index
t=(1,2,3,4,5)
print(t[2])
print(t[-3])

# membership operator
t=(1,2,3,4,5)
print(2 in t)
print(-3 not in t)

#iteration
t=(1,2,3,4,5)
for i in t:
    print(i)

    # any one we can use
    
for i in (1,2,3):
  print(i)    
  
  
  # slicing
t=(1,2,3,4,5)
print(t)
print(t[::-1])
print(t[:-1])
print(t[1:5])
print(t[1:5:2])

# tuples methods index,tuple length,count,copy
t=(1,2,3,4,5)
print(t.index(2)) # index
print(len(t))     #tuple length
print(t.count(2)) #count
t2 = t
print(t2)     # copy


# zip method in tuples
t1=(1,2,3,4)
t2=(5,6,7,8,7)
t3=(tuple(zip(t1,t2)))
print(t3)
