empty_list=[]

weekday=["sunday","Monday","Tuesday","Wednesday"]

# List is mutable that means you can add or delete the data the existing list.

weekday[3]="test"

print(weekday)

# converting the string to a list

k="abcd"

print(k)

b=list(k)

print(b)

a=["p","b","c"]

b=["g","h","j"]

c=["c","o"]

w=a+b+c # it is like joining

z=[a,b,c] # it like adding list inside a list

print("Print w",w)

print("printing z",z)

print(z[1])

print(w[1])

# note the difference between the last 2 statements

print(len(z))

z.append("prabha")

print("Updated Z is",z)

print(len(z))

weekday.insert(2,"dummy")

print(weekday)


weekday.remove("dummy")

print(weekday)

weekday.pop()
print("printing weekday",weekday)
weekday.pop()

print("printing weekday",weekday)

weekday.pop(1)

print("printing weekday",weekday)

del weekday[0]

print("printing weekday",weekday)

weekday=["sunday","Monday","Tuesday","Wednesday"]

print("printing weekday",weekday)

weekday.clear()
print("printing weekday after clear",weekday)

weekday=["sunday","Monday","Tuesday","Wednesday"]

# to find the index of certain element
print(weekday.index('Monday'))

# to check an element is present in list
print('Monday' in weekday)

print('Friday' in weekday)

weekday.extend('Saturday')

print(weekday)

print(weekday.copy())


print("Checking the functions")


weekday.reverse()
print(weekday)

weekday.sort()

print(weekday)


dd=["prabha","Bharath","Vijay","vijay","Abi","Vijay"]

print(dd.count("Vijay"))


dd.sort()
print(dd) # sorting start with capital letter and then with small letter

num=[1,2,3,4,5,6,7,9,8]

num.sort()

print(num)

num.sort(reverse=True)

print("After reverse",num)

n1=[1,2,3,4,5,6]
n2=n1

print(n1)
print(n2)

n1[1]='prabha'

print(n1)
print(n2)

n2[4]="karan"

print(n1)
print(n2)

# here n1 and n2 are in synchronous whenever the change happens in one variable it affects the other.

# inorder to do the shallow copy to other variable use copy fuction

n1_copy=n1.copy();

print(n1_copy)

n1_copy[3]="oops"

print(n1)
print(n1_copy)
