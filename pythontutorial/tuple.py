# tuple is like list but it is immutable
t="hello"
t1=()

# list we use [] but for tuple we use ()

t1=("prabha","Aalia","Little","Pie")

a,b,c,d=t1

print(a)

print(type(t))
print(type(t1))

t2="hello","prabha","Raj" # it automatically converst taht to a tuple. If it's only one string that it is considered as string

print(t2)

# converting the list to tuple


dd=["prabha","Bharath","Vijay","vijay","Abi","Vijay"]

print(dd)
tuple(dd)

x=tuple(dd)

print(x)

# tuple allows only 2 funtion count() and index()

print(dd.count('Vijay'))

print(dd.index('Bharath'))

len(dd)

'prabha' in dd

