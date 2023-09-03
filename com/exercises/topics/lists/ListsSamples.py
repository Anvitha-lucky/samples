import math
import random

import numpy as np

#Write a Python CODE to sum all the items in a list.

list1=list([1,2,3,4,5,6,7,3,2,5,6,9])
# simple way using sum librany function
print(math.fsum(list1))
#using standard library functions
print(sum(list1))
#using for loop
summation=0
for el in list1:
    summation+=el
print(summation)


#Write a function to find the maximum element in a list.

def findMax(elements):
    return max(elements)
print(findMax(list1))

def findMax1(elements):
    return sorted(elements,reverse=True)[0]
print(findMax1(list1))


# Write a program to reverse a list.

print(list1[::-1]);
for ll in reversed(list1):
    print(ll)
print("**************************************")
reversed_list = list(reversed(list1))
print(reversed_list)

# reverse a String
my_string = "Hello, World!"

reversed_string = ''.join(reversed(my_string))
print(reversed_string)
print(my_string[::-1])

# Write a function to find the common elements between two lists.

list2=list([3,4,7,11,33,24,2,11,45,46])

print(np.intersect1d(list1,list2))

def findCommonElements(l1,l2):
    commons=[]
    for i in l1:
        if i in l2:
            if i not in commons:
                commons.append(i)
    return commons
print(findCommonElements(list1,list2));

# Write a program to remove duplicates from a list.

def removeDuplicates(l1):
    deduplicatedList=[]
    for i in l1:
        if i not in deduplicatedList:
            deduplicatedList.append(i)
    return deduplicatedList
print(removeDuplicates(list1))
print(removeDuplicates(list2))

print(list(set(list1)))
print(list(set(list2)))

#Write a function to check if a list is empty.

def emptyChecker(listToCheck):
    return len(listToCheck)
if emptyChecker([]) <=0:
    print(" List is empty ")
else:
    print("List is not empty")

#Write a program to merge two lists into a single list.


print(list1+list2)

# another way to merge lists
for element in list2:
    list1.append(element)
print(list1)

#another way is extending list

list1.extend(list2)
print(list1)

# Write a function to find the index of a specific element in a list.

def getIndexesOfAnElementInList(elements,elementToFindIndex):
    indexes=[]
    for position in range(len(elements)):
        if (elements[position]==elementToFindIndex):
            indexes.append(str(position))
    return indexes
print("element {} find in following indexes".format(2),",".join(getIndexesOfAnElementInList(list1,2)))

#Write a program to count the occurrences of an element in a list.
def getCountOfOccurencesOFAnElement(elements,elementToFind):
    count=0
    for position in range(len(elements)):
        if elements[position]==elementToFind:
            count+=1
    return count
print( getCountOfOccurencesOFAnElement(list1,2))

print(list1.count(2))
print(len([item for item in list1 if item == 2]))

# Write a function to sort a list in ascending order.

#we can implement all sorting techniques to sort elements in list but for now we can utilize existing librabry functions

list1.sort(reverse=True)
print(list1)
list1.sort(reverse=False)
print(list1)
list1.sort()
print(list1)
print(sorted(list1))
print(sorted(list1,reverse=True))

# Write a program to shuffle a list randomly.

random.shuffle(list1)
print(list1)

# Write a function to find the second largest element in a list.

def findSecondLargest(elements):
    if len(elements)>0:
        elements=list(set(elements))
        elements.sort()
        return elements[-2]
    else:
        return -1
print("*******************     ",findSecondLargest(list1))

#Write a program to split a list into smaller lists of a specified size.

def sliceTheListIntoSpecificSize(elements,size):
    masterList=[]
    for i in range(0,len(elements),size):
        masterList.append(elements[i:i+size])
    return masterList

print("*******************     ",sliceTheListIntoSpecificSize(list1,4))

print([list1[x:x+4] for x in range(0, len(list1), 4)])

#Write a function to check if a list is a palindrome.

templist=['l','i','r','i','l']
print(templist==templist[::-1])
print(templist==list(reversed(templist)))

#Write a program to find the intersection of two lists.
# findCommonElements() covers this

print([val1 for val1 in list1 if val1 in list2])
print(list(set(list1)&(set(list2))))
print(set(list1).intersection(set(list2)))

# def intersection(lst1, lst2):
#     lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
#     return lst3


# from functools import reduce
# intersection = reduce(lambda acc, x: acc + [x] if x in list2 and x not in acc else acc, list1, [])

#Write a function to remove all even numbers from a list.

# def removeevenElements(elements):
#
#     for element in elements:
#         if element % 2 == 0:
#             elements.remove(element)
#     return elements
def removeevenElements(elements):
    for element in elements.copy():
        if element % 2 == 0:
            elements.remove(element)
    return elements
print(">>>>>>>>>>>>>",removeevenElements(list2))
print([i for i in list2 if i % 2 != 0])


list3=random.sample(range(1,100),50)
print(list3)

print([random.randrange(1,50,3) for i in range(50)])

lis = []
for _ in range(10):
    lis.append(random.randint(0, 51))
print(lis)


print(random.sample(range(1,22),20))

print([random.randrange(1,50,3) for i in range(50)])