# set is like the dictionary created with {} but it has no key value pair

empty_set={}

print(type(empty_set))

empty_set=set()

print(type(empty_set))

set1={"r","t","y","m"}

print(set1)

dic4={4:"prabh",5:"prabha",6:"kuruvi"}

set2=set(dic4)

print(set2)

set3=set(dic4.values())

print(set3)

print(len(set3))

print("prabh" in set3)

set3.add("scott")

print(set3)

# doesn't support the indexing Eg: set3[6]

print("diff")
print(set3.difference(set2))  # to find the difference between the set


# set method

print(set3.intersection(set2)) # common element between 2 sets

set3.difference_update(set2) # it deltes the common element between 2 sets and return the rest from first set

print(set3.isdisjoint(set2)) # to check there is no common elment between 2 set