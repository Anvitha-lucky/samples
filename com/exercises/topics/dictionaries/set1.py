#Write code to merge two dictionaries.
import random

dict1={'a':4,'b':2,'c':6}
dict2={'d':3,'e':5,'f':1}

dict2.update(dict1)
print(dict2)

#How can you remove a key from a dictionary?
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print(my_dict)

#Write a function to find the highest value in a dictionary.
print(max(dict2.values()))

#How do you check if a key exists in a dictionary?
print( 'd' in dict2)

#Write a function to count the frequency of each element in a list and store it in a dictionary.

from collections import Counter

ll=[random.randrange(1,20,3) for i in range(20)]
print(ll)
for item in Counter(ll).items():
    key,value=item
    print(key,'repeated',value,'Times')

print(ll)
print(sorted(set(ll),key=ll.index))
print(sorted(set(ll),key=ll.index,reverse=True))
print(sorted(set(ll),reverse=True))

#Write a function to sort a dictionary by its values in descending order.
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(dict2)
print(sorted(dict2))
print(dict(sorted(dict2.items(),key=lambda x:x[1])))
print(dict(sorted(dict2.items(),key=lambda x:x[0])))

# How can you iterate through the keys and values of a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

#How can you create an empty dictionary?

emptydict=dict()
emptydict1={}

print(dict2)
print( min(dict2, key=dict2.get))

print(dict1)
print( max(dict1, key=dict1.get))

# Write a function to remove duplicate values from a dictionary.

sample={}
sample['a']=1
sample['']=2
sample['']=3
sample[None]=4
print(sample)

test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print(res)

# Method #2: Using dictionary comprehension
temp = {val: key for key, val in test_dict.items()}
print(temp)
res = {val: key for key, val in temp.items()}
print("The dictionary after values removal : " + str(res))

#Method 3: use the setdefault() method.
print("____________________________________________________________")
res = {}
for key, val in test_dict.items():
    res.setdefault(val, key)
print(res)
res=dict((v, k) for k, v in res.items())
print(res)
print("_________________________________________________________________________________")
vals_dict = dict.fromkeys(test_dict.values(), None)
print(vals_dict)
for key, val in test_dict.items():
    if vals_dict[val] is None:
        vals_dict[val] = key
print(vals_dict)

print(len(my_dict))

print(dict1==dict2)

#How can you create a dictionary with default values for missing keys?

from collections import defaultdict

default_dict = defaultdict(int)  # Default value for missing keys is 0
default_dict['a'] = 1
print(default_dict['a'],default_dict['b'])  # Accessing a missing key returns the default value (0)
