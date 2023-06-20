#
#
# # This comment
# print("THis is my first program")
#
# # Variables
# #no need to define data type
#
# name="swapnil"
#
# print(type(name))
#
# name=1
#
# print(type(name))
# name=1.2
#
# print(type(name))
#
# name=False
#
# print(type(name))
#
# print("*********************Special data type**********************")
# # Special data type
# name={}
# print(type(name))
# name=[]
# print(type(name))
# tup=(1,2,3)
# print(type(tup))


print("****************Operators********************************")

a=20
b=20

#Comparison operator
print(a==b)

# Assignment
c=a
print(c)

# Addition
c=a+b
print(c)


# Sub
c=a-b
print(c)

# Division
c=a/b
print(c)

# Module
c=a%b
print(c)

# is

print(a is  b)

print("ukugugkugujbjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjnkhghgjhghgjhjh")
#And,OR,Not
a=False
b=False
print(a or b)
print(a and b)
print(not a) #id not null

print("THis is statement one yyj",end=" ")

print("THis is statement two",end=" ")
print("THis is statement two")

a=20
b=20

d=5
e=5
print(a==b)

if a==b:
    print("I am adding a and b")
    c=a+b
else:
    print("i am sub a and b")
    c=a-b

if a==b:
    print("I am adding a and b")
    c=a+b
elif d==e:
    c=d+e

if a==b:
    print("if without else")

print("value of c={},d={}".format(c,d))
print("{}{}{}{}".format(a,b,c,d))
s="i am swapnil {}"

print(s.format(a))

print(f"{a}shhdsf{b}sdfsdf{c}sdfdf{d}")

#while
#for

#List
#Dict
#tuple
#set

# while <condition>:
#     operation

i=0

while i<=6:
    print(i)
    if i==4:
        i = i + 1
        continue #It will continue to next iteration
    if i==4:
        print("i am in if condition")
        break   #It will reak the loop
    else:
        print("i am in else")
    i=i+1
else:
    print("Value of i={}".format(i))


# For loop
#for variable in condiftion

#what is diff between range and xrange
for i in range(2,10):
    if (i==8):
        print("in if")
        break
    else:
        print("in else")


# List
# Veriable name=[]

l1=[1,2,5,6,"test1","test2",1.2,True,False,2,5]

print(l1)
print(type(l1))

l1.append("added")
print(l1)
print(l1.pop())  #what is pop function remove last element from the list and return that element
print(l1)
l1.remove("test2")  # remove element from the list
print(l1)
print(l1.count("test1"))

# l1=[2,4,7,8,9,1,2,3,45]
# l1.sort()
# print(l1)

for i in l1:
    print(i)
    if i == 'test1':
        l1.append("after If")
        break



print(l1)

print(l1[3])

a=10
b=a
print(b)
print(a)
a=20
print(b)
print(a)


# Shallow copy and Deep copy difference
l2=l1
print(l2)
l1.append("app")
print(l1)
print(l2)

l2.append("app2")
print(l1)
print(l2)

print("Deep copy")

#Deep copy
l1=l2.copy()
print(l1)
print(l2)

l2.append("app3")

print(l1)
print(l2)

l3=l1+l2 #add element from 2 different list
print(l3)

l1="chandh"
l2="ddf"

print(l1)
print(l2)


# Remove duplicate elements
l1=[1,2,3,3,2,1,4,5,4]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

# Tuple,Set,dictionary

# What is difference between list and tuple
# Tuple
tup=(1,2,3,4,5)

print(type(tup))

for i in tup:
    print(i)

# Set
# set does not allow duplicate element

set_1={2,3,1,4,6,7}
print(set_1)

set_1.add(3)
print(set_1)

# Remove duplicate element using set
l1=[1,2,3,3,2,1,4,5,4]
print(set(l1))

s2=set(l1)
print(type(s2))
print(s2)

l2=list(s2)
print(l2)
print(type(l2))

l3=tuple(l2)
print(type(l3))
print(l3)

i=1
print(type(i))

j=str(i)
print(type(j))
print(j)
print(int(j))

j="1"
k=int(j)+1
print(int(j))


# Dictionry
#username,password,address
l1=["ss",1212,"add"]
dict2={121}
print(type(dict2))
dict1={"username":"ss","password":1212,"address":"add"}
print(dict1)
print(dict1.get("username"))
print(dict1.pop("password"))
print(dict1)
#print(dict1.popitem())

dict1["pass"]="this is pass"
print(dict1)

dict1.update({"address":"address1212"})
print(dict1)
dict1["address"]="updated"
print(dict1)

print(type(dict1.keys()))

for i in dict1.keys():
    if i=="pass":
        print(dict1[i])
        #assert dict1[i]==1212,"password not matching"

print(dict1)
for i,j in dict1.items():
    print("this is key",end=" ")
    print(i)
    print("this is value",end=" ")
    print(j)


dict3={"address":"address1212","names":["a","sdsdsd","sdsdsd","hjhhjhj"],"marks":{"math":12,"sci":45,"bio":99,"listmarks":[12,45,99],"internal":{"math":2323,"dfdf":2323}}}

for i in dict3['names']:
    print(i)

for i,j in (dict3["marks"]).items():
    print(f"marks {i}={j}")

print(dict3['marks']['listmarks'])
print(dict3['marks']['internal']['math'])

pet_data=[
    {
        "id": 503,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "albin",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333894,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333895,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333896,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333897,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333898,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333899,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333900,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333901,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333906,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333907,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333908,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333909,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333910,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333911,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333912,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333913,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333914,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333915,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333916,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333917,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333918,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333920,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333924,
        "category": {
            "id": 0,
            "name": "local"
        },
        "name": "ex",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333925,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333927,
        "category": {
            "id": 0,
            "name": "fish"
        },
        "name": "Лящ",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333928,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 125846,
        "category": {
            "id": 0,
            "name": "fish"
        },
        "name": "Лящ",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333937,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333960,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 12,
        "category": {
            "id": 1,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 1,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333964,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333967,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333972,
        "category": {
            "id": 0,
            "name": "mammiferi"
        },
        "name": "gatto",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333978,
        "category": {
            "id": 0,
            "name": "mammiferi"
        },
        "name": "gatto",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333980,
        "category": {
            "id": 0,
            "name": "mammiferi"
        },
        "name": "gatto",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333981,
        "category": {
            "id": 0,
            "name": "mammiferi"
        },
        "name": "gatto",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333982,
        "category": {
            "id": 0,
            "name": "mammiferi"
        },
        "name": "gattoo",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333987,
        "category": {
            "id": 54510383,
            "name": "cillum elit"
        },
        "name": "doggie john",
        "photoUrls": [
            "eiusmod anim",
            "ut dolore labore ut"
        ],
        "tags": [
            {
                "id": -44902202,
                "name": "esse nostrud in in dolor"
            },
            {
                "id": 63649408,
                "name": "enim commodo irure"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333988,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333989,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333990,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333991,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333992,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333993,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854333996,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334001,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334002,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334003,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334005,
        "category": {
            "id": 54510383,
            "name": "cillum elit"
        },
        "name": "doggie jon",
        "photoUrls": [
            "eiusmod anim",
            "ut dolore labore ut"
        ],
        "tags": [
            {
                "id": -44902202,
                "name": "esse nostrud in in dolor"
            },
            {
                "id": 63649408,
                "name": "enim commodo irure"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334012,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334013,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334014,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334018,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334021,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334022,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334023,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334024,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334025,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334026,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334027,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 567833,
        "category": {
            "id": 77,
            "name": "endemics"
        },
        "name": "badger",
        "photoUrls": [
            "https://i.pinimg.com/originals/09/7d/0f/097d0fbfcfefd19ccad5e9e352479a5b.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334028,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334029,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 112233,
        "category": {
            "id": 30,
            "name": "Eq-dog"
        },
        "name": "Postman",
        "photoUrls": [
            "URLLink"
        ],
        "tags": [
            {
                "id": 10,
                "name": "Doberman"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334040,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 5555465667756,
        "category": {
            "id": 333,
            "name": "dragon"
        },
        "name": "fire",
        "photoUrls": [
            "https://avatars.mds.yandex.net/i?id=078921257ab65d7482122d84f409d944-6609300-images-thumbs&n=13"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334041,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334044,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 8042831,
        "category": {
            "id": 2,
            "name": "Рыжик"
        },
        "name": "Cats",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 8042830,
        "category": {
            "id": 2,
            "name": "Рыжик"
        },
        "name": "Cats",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334053,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334055,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334056,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334057,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334058,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334059,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334060,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334061,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334062,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334063,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334064,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334065,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334066,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334067,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334068,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334069,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334070,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334074,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334075,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334076,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334080,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 123456,
        "category": {
            "id": 0,
            "name": "fish"
        },
        "name": "Лящ",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334081,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334087,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334088,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334096,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334098,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 6666,
        "category": {
            "id": 666,
            "name": "string"
        },
        "name": "Doodlie",
        "photoUrls": [
            "https://cdn.fakercloud.com/avatars/maxlinderman_128.jpg"
        ],
        "tags": [
            {
                "id": 5,
                "name": "Selling"
            }
        ],
        "status": "available"
    },
    {
        "id": 5031,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "albin",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334109,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "sunny",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334110,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334112,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334118,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334129,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334130,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334131,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334132,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334133,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334134,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334135,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334136,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334137,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334138,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334139,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334140,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334141,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334142,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334143,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334144,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334145,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334146,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334147,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334148,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334149,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334150,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334151,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334153,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 2210,
        "category": {
            "id": 2210,
            "name": "Dogearmy"
        },
        "name": "DogeArmy",
        "photoUrls": [
            "www.dogearmy.org"
        ],
        "tags": [
            {
                "id": 2210,
                "name": "Dogearmy"
            }
        ],
        "status": "available"
    },
    {
        "id": 1245,
        "category": {
            "id": 1245,
            "name": "xyz"
        },
        "name": "xyz",
        "photoUrls": [
            "test"
        ],
        "tags": [],
        "status": "available"
    },
    {
        "id": 9223372036854334172,
        "category": {
            "id": 0,
            "name": "dogs"
        },
        "name": "qa_doggie",
        "photoUrls": [
            "image.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "qa_tag"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334173,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Кузя Кузьмин",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334175,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334176,
        "category": {
            "id": 0,
            "name": "horse"
        },
        "name": "dayn",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334177,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334178,
        "category": {
            "id": 0,
            "name": "dogs"
        },
        "name": "qa_doggie",
        "photoUrls": [
            "image.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "qa_tag"
            }
        ],
        "status": "available"
    },
    {
        "id": 2323,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "dog",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "tomy"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334179,
        "category": {
            "id": 8212614,
            "name": "voluptate ea qui sint"
        },
        "name": "doggie",
        "photoUrls": [
            "quis Lorem Duis aute",
            "veniam nulla culpa"
        ],
        "tags": [
            {
                "id": -42092226,
                "name": "labore"
            },
            {
                "id": -72688380,
                "name": "consectetur sint qui"
            }
        ],
        "status": "available"
    },
    {
        "id": 345,
        "category": {
            "id": 0,
            "name": "Fish"
        },
        "name": "Nemo",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334189,
        "category": {
            "id": -71366914,
            "name": "minim cillum dolor eiusmod"
        },
        "name": "doggie",
        "photoUrls": [
            "laborum ullamco ipsum ut",
            "nisi sunt est culpa"
        ],
        "tags": [
            {
                "id": 72480827,
                "name": "commodo"
            },
            {
                "id": 75675067,
                "name": "re"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334199,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334200,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334201,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334202,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334203,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334204,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334205,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334206,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334207,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334208,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334209,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334210,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334211,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334212,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334213,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334214,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334215,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334216,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334217,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334218,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334219,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334222,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334225,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334229,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334230,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334231,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334232,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334235,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334239,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "sunny",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334240,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334245,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334246,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334251,
        "category": {
            "id": 0,
            "name": "Evgeny"
        },
        "name": "Lord",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334259,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334260,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334261,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334262,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334263,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334264,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334265,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334268,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334269,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334270,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334271,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334272,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334273,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334274,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334275,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334276,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334277,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334278,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334279,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334280,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334281,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334282,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334283,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334305,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334307,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334314,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334315,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334319,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334320,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334321,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334322,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334323,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334324,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334326,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334327,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334328,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334329,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334330,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334331,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334332,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334333,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334334,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334335,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334336,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334337,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334338,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334339,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334340,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9222968140497180179,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "test",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334347,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334348,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334349,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334350,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334351,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334352,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334353,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334354,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334356,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334357,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334362,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334363,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 1234,
        "category": {
            "id": 0,
            "name": "Oli"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334390,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334391,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 1709,
        "category": {
            "id": 1709,
            "name": "horse"
        },
        "name": "rainbow pony",
        "photoUrls": [
            "https://i.pinimg.com/originals/62/a8/1a/62a81a8baed5d17542e152a488fd1217.jpg"
        ],
        "tags": [
            {
                "id": 1709,
                "name": "pony"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334399,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334400,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334401,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334402,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334403,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334404,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334405,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334406,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334407,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334408,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334410,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334411,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334412,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334414,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334417,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334418,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334419,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334422,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334423,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334424,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334425,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334426,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334427,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334451,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334452,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334453,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334454,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334455,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334456,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334457,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334458,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 1986,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": "Asya",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 274,
        "category": {
            "id": 222,
            "name": "cat"
        },
        "name": "barsick",
        "photoUrls": [
            "https://versiya.info/uploads/posts/2020-01/1578642390_photo_2020-01-10_17-44-28.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334464,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 55,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "VssAdministrator",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334472,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334475,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334477,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334478,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334479,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334480,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334481,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334482,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334483,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334487,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334488,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334489,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334490,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334491,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334492,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334495,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334496,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334497,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334498,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334499,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334500,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334501,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334504,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334505,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334514,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334515,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334516,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9222968140491042131,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334522,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334525,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334531,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334532,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334533,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334534,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334535,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334536,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334537,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334538,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334539,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334540,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334542,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334543,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334544,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334546,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334547,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334548,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334549,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334550,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334551,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334552,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334553,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334554,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 1332,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "murka",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334563,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 6678644543,
        "category": {
            "id": 888,
            "name": "cat"
        },
        "name": "Goose",
        "photoUrls": [
            ">https://static.wikia.nocookie.net/marvelcinematicuniverse/images/c/cd/Goose_Textless_Poster.jpg/revision/latest?cb=20210509040815"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334586,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334588,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334589,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334590,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334591,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 2016,
        "category": {
            "id": 0,
            "name": "yzogaapmer"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334592,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334593,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 200,
        "category": {
            "id": 200,
            "name": "swagger20"
        },
        "name": "swagger20",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 200,
                "name": "swagger20"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334597,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334598,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334599,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334600,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334601,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334602,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334603,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 199,
        "category": {
            "id": 0,
            "name": "german"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334604,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334605,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334606,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334607,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334608,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334609,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334610,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334611,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334612,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334613,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334614,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334615,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334616,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334617,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334622,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334623,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334624,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 5556,
        "category": {
            "id": 77,
            "name": "endemics"
        },
        "name": "badger",
        "photoUrls": [
            "https://i.pinimg.com/originals/09/7d/0f/097d0fbfcfefd19ccad5e9e352479a5b.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334630,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 8118,
        "category": {
            "id": 888,
            "name": "doggy"
        },
        "name": "buba",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334633,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334635,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334649,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 667843,
        "category": {
            "id": 888,
            "name": "cat"
        },
        "name": "Goose",
        "photoUrls": [
            ">https://static.wikia.nocookie.net/marvelcinematicuniverse/images/c/cd/Goose_Textless_Poster.jpg/revision/latest?cb=20210509040815"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334655,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334656,
        "category": {
            "id": 11,
            "name": "Perro"
        },
        "name": "Ignacio",
        "photoUrls": [
            "Ignacio photo"
        ],
        "tags": [
            {
                "id": 12,
                "name": "Raza"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334657,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334663,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334664,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334665,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334666,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334667,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334668,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334669,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334670,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334671,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334672,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334673,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334674,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334675,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334676,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334677,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334678,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334679,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334680,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334681,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334682,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334684,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334685,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334690,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334694,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334695,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334696,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334697,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334698,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334699,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334700,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334701,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 5555465667757,
        "category": {
            "id": 333,
            "name": "dragon"
        },
        "name": "fire",
        "photoUrls": [
            "https://avatars.mds.yandex.net/i?id=078921257ab65d7482122d84f409d944-6609300-images-thumbs&n=13"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334715,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334718,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334719,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334720,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334730,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334731,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334732,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334733,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334734,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334735,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334736,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334738,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334739,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334740,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334742,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334743,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334744,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334747,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334748,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334749,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334750,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334753,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334754,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334755,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334756,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334757,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334758,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334759,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334764,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "newPet",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334765,
        "category": {
            "id": 777,
            "name": "string"
        },
        "name": "Mars",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 566767787,
                "name": "zinaa"
            }
        ],
        "status": "available"
    },
    {
        "id": 1036,
        "name": "string",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    },
    {
        "id": 9223372036854334767,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "newPet",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334772,
        "name": "doggie",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    },
    {
        "id": 9223372036854334775,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334777,
        "name": "doggie",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    },
    {
        "id": 9223372036854334780,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334782,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334783,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 6521,
        "category": {
            "id": 15,
            "name": "DOG"
        },
        "name": "TIGRA",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 5,
                "name": "DOGFAT"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334785,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334786,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "notavailable"
    },
    {
        "id": 20221111,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Дядя_Паша",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Дворняга"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334795,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "fish",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    },
    {
        "id": 9223372036854334808,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
]

print(len(pet_data))
#Get all pets with available status
#Check status of each pet is available or not
for i in pet_data:
    if i['status'] != "available":
        assert i['status'] == "available" , "status is not correct for id {} status should be available but showing {}".format(i["id"],i["status"])