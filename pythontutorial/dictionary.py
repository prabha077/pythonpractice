# dictionary is the another data type in python which like key value map. It can be declared with curly braces

empty_d={}


dic={"b":"Bruce","c":"charles","d":"Dog"}

print(dic)
print(type(dic))

lst=[[1,'3'],[2,'4'],[5,'6']]

print(lst)

print(lst[1])

t=dict(lst)

print(t)

# like wise you shall convert the dict to list and list to dict and tuple to dict and dict to tuple viceversa

# it will not allow duplicate key as like hash map. If you define same key again the latest one will replace the old one

t["7"]="prabha"  # adding new key value to the existing dictionary

print(t)

print(t["7"])


#updating the exisitn dictionary

dic1={1:"prabha",2:"karan",3:"nambi"}

dic2={4:"prabhaaa",5:"karannn",6:"nambiii"}

dic2.update(dic1) # adding the second dic2 value into the first one

print(dic2)

dic3={4:"prabh",5:"prabha",6:"kuruvi"}

dic2.update(dic3)

print(dic2)

print(dic3)

#to delte the content of the dictionar

del dic3[6]

print(dic3)

dic3.clear(); # to clear the content but keep the dict

print(dic3)

# to delte the whole dictionary


print("After delete")

#del dic3

#print(dic3)


dic4={4:"prabh",5:"prabha",6:"kuruvi"}

dic4.get(6)

print(dic4.get(6))

print(4 in dic4)

print("prabha" in dic4)

print(dic4.keys())

print(dic4.values())

diclistkeys=list(dic4.keys())

print(diclistkeys)

# the synchronus and copy method that we did for list apply to the dictionary too

#a=b when cahnge happens to a it will be affect to b also

