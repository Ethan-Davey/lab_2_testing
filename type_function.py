#Type Functions
a = 11
print(type(a))
a = 11.0
print(type(a))
a = "11"
print(type(a))
a = "11" + "11"
print(type(a))
a = "a"
print(type(a))
a = True
print(type(a))
a = "False"
print(type(a))

#Type Conversion

x = 10.5
print(type(x))
x = 10.5
x = int(x)
print(type(x))

x = "Hello"
y = 10
z = 5.5
print(type(x))
print(type(y))
print(type(z))
print(y+z)
print(type(y+z))
print(y+int(z))
print(type(y+int(z)))
print(z+float(y))
print(type(z+float(y)))
z = str(z)
print(type(z))
print(x+str(y)+str(z))
print(type(x+str(y)+str(z)))
print (x+y)