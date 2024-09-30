# operations on sets
# union
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))

# or

print(s1|s2)

# intersection
s1={1,2,3,4}
s2={5,6,7,4}
print(s1&s2)

# difference
s1={1,2,3,4}
s2={5,6,7,1,2,3}
print(s1-s2)

# set symmetric difference
s1={1,2,3,4}
s2={5,6,7,1,2,3}
print(s1^s2)

# membership operators
s1={1,2,3,4}
print(1 in s1)
print(5 not in s1)

# set methods add,clear,discard,remove,pop,copy,difference,symmetric difference,intersection,union
s={1,2,3,4}
s.add(5) # add
print(s)

s.clear() # clear
print(s)
s2={1,2,3,4}


s2.discard(2) # discard
print(s2)
s1={1,2,3,4}


s1.remove(1) # remove
print(s1)


s4={3,4}
s4.pop() # pop
print(s4)

s5={1,2,3,4}
s5.copy() # copy
print(s5)

s6={1,2,3,4}
s7={3,4,5,6}
print(s6.difference(s7)) # difference


a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b)) # symmetric difference

c={1,2,3,4}
d={3,4,5,6}
print(c.intersection(d)) # intersection

e={1,2,3,4}
f={3,4,5,6}
print(e.union(f)) # union




