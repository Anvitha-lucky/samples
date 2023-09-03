
import random

list1=list(random.sample(range(1,31),20))
list2=list([random.randrange(1,10,3) for i in range(25)])
# problem statement 1:  find the length of list
#method 1
print(len(list1))
print(len(list2))

#method 2
print(list1.__len__())

# important point to remember her is  __len__() is used to change the behaviour to len() in custome implementatiosn

#method 3
def getsize(elements):
    counter=0
    for element in elements:
        counter+=1
    return counter;
print(getsize(list1))
print(getsize(list2))

# method 4
print("********************************************************************************")
print(sum(1 for element in list1))
print("********************************************************************************")

# problem statement 2: Sum of List: Write a function to find the sum of all elements in a list.
#method 1
print(sum(element for element in list1))

#method 2

print(sum(list1))

#method 3

def addelements(elements):
    total=0;
    for element in elements:
        total+=element
    return total
print(addelements(list1))
print(addelements(list2))

# problem statement 3: Largest Element: Find the largest element in a list.
print(list1)
print(max(list1))
print(max(list2))
print(sorted(list1,reverse=True)[0])
print(sorted(list1,reverse=False)[-1])
print(list1)
list1.sort(reverse=True)
print(list1)  # i.e

#List Reversal: Reverse a list without using built-in function

print(list1[::-1])
print(list1)
tempList=list()
for element in range(len(list1)-1, -1, -1):
    tempList.append(list1[element])
print(tempList)

# problem statement :5 Remove Duplicates: Remove duplicates from a list while preserving the order.
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(list1)
print(list2)
print(dict.fromkeys(list2))
print(list(dict.fromkeys(list2)))
print(list(set(list2)))
#Time Complexity: O(n)
#Space Complexity: O(n)

# using list comprehension
list3=[random.randrange(1,20,3) for i in range(25)]
print(list3)
resultList=[]
[resultList.append(x) for x in list3 if x not in resultList]

print(resultList)

#Time Complexity: O(n)
#Space Complexity: O(n)
print("******************************************************************************************")
print(list1[:10])
print(list1[:2])

print([i for n, i in enumerate(list3) if i not in list3[:n]])
print([i for n, i in enumerate(list1) if i not in list1[:n]])

#Time Complexity: O(n^2)
#Space Complexity: O(n)

# using collections.OrderedDict.fromkeys()
from collections import OrderedDict
print("%%%%%%%%%%%%%",list(OrderedDict.fromkeys(list3)))

res = []
for i in list3:
    if i not in res:
        res.append(i)
print(res)
# using collections.Counter.fromkeys()
from collections import Counter
print(list3)
temp = Counter(list3)
print("&&&&&&&&",temp)
res = [*temp]
print(res)

import numpy as np
res = np.unique(list3)
print(res)

#Count Occurrences: Count the number of occurrences of a specific element in a list.
print(Counter(list3).get(4))
print(Counter(list3)[4])
print(list3.count(4))

import operator
print(operator.countOf(list3,4))

print(len([i for i in list3 if i==4]))
#count the occurences of all values
from collections import Counter
print(Counter(list3))
print(list3)
list3.pop()
print(list3)
print(list3[:])

#List Comprehension: Create a new list with squares of elements from an existing list.

print([i**2 for i in list3])

#List Concatenation: Concatenate two lists.
print(list1+list3)
list1.extend(list3)
print(list1)

def listAppend(l1,l2):
    for i in l2:
        l1.append(i)
    return l1
print(listAppend(list1,list3))
print(list1)

# problem statement Sort List: Sort a list in ascending order.
temp=np.unique(list1).tolist()
print(temp)
print(sorted(temp,reverse=True))
print("************************************************")
print(temp)
temp.sort(reverse=True)
print(temp)

# Split List: Split a list into smaller lists of a specified size.

print([ list1[i:i+5] for i in range(0,len(list1),5)])

# Find Median: Find the median of a list of numbers.

def findMedian(lst):
    sorted_lst = sorted(lst)
    print(sorted_lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]
print(list3)
print(findMedian(list3))

#Remove Negatives: Remove all negative numbers from a list.

def removeNegatives(lst):
    return [x for x in lst if x >= 0]
print(removeNegatives([1,3,-2,3,-5]))
#List Rotation: Rotate a list to the left by a given number of positions.

def rotateElementsToLeft(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]
print("@@@@@@@@@@@@@@@@@@@@@@@@",list3)
print(rotateElementsToLeft(list3,4))
print(list3)
#Rotate Elements to right
print("@@@@@@@@@@@@@@@@@@@@@@@@",list3)
# def rotateListToRight(lst, n):
#     n = n % len(lst)
#     print(lst[n:])
#     print(lst[:n])
#     return lst[:n]+lst[n:]
#
# print(rotateListToRight(list3,5))

#Frequency Distribution: Create a dictionary with the frequency of each element in a list.

from collections import Counter
print(Counter(list3))

#Method 2

def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))
print(CountFrequency(list1))

def secondWayCountFreequency(lst):
    freeq={}
    for i in lst:
        freeq[i]=lst.count(i)
    for key,value in freeq.items():
        print(key,'---->',value)
secondWayCountFreequency(list1)


def CountFrequency2(my_list):
    # Creating an empty dictionary
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count
print(CountFrequency2(list1))

import operator

def CountFrequency3(my_list):

	# Creating an empty dictionary
	freq = {}
	for items in my_list:
		freq[items] = operator.countOf(my_list, items)

	for key, value in freq.items():
		print("% d : % d" % (key, value))

CountFrequency3(list1)


# problem statement: Unique Permutations: Generate all unique permutations of a list.
from itertools import permutations
print(list(set(permutations([1,2,3,6]))))

#List Intersection: Find the intersection of multiple lists.
def list_intersection(*lists):
    return list(set.intersection(*map(set, lists)))

print(list_intersection(list1,list3,list2))

#List Flattening: Flatten a nested list.

def flatten_list(nested_lst):
    flatlist = []
    for sublist in nested_lst:
        if isinstance(sublist, list):
            flatlist.extend(flatten_list(sublist))
        else:
            flatlist.append(sublist)
    return flatlist

def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))
print("*****************************   ",list_difference(list1,list2))