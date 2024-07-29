
# write a program to check whether triangular is valid or not if sides are given
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
if a+b>c and a+c>b and b+c>a:
    print("triangle is valid")
else:
    print("triangle is not valid")


output:
enter a5
enter b7
enter c10
triangle is valid
