#1. check if a string is palindrome or not
import random

str="liril"
def isPalindrome(str1):
    if str1==str1[::-1]:
        return True
    else:
        return False

print(isPalindrome(str))

#Count Vowels and Consonants

def countThevowelsAndConsonents(st):
    matchString="AEIOUaeiou"
    vowelsCount= sum([1 for ch in st if ch in matchString])
    consonentCount=len(st)-vowelsCount
    return vowelsCount,consonentCount

print(countThevowelsAndConsonents("Lakshmi Narayana Reddy Dwarampudi"))

# problem statement: Check Anagrams

def checkAnagram(str1,str2):
    return sorted(str1)==sorted(str2)

print(checkAnagram("lakshmi","shakiml"))

# rempove duplicates

def removeDuplicates(s):
    return ''.join(sorted(set(s),key=s.index))
print(removeDuplicates("lakshmi Narayana Reddy"))

print([random.randrange(1,30,2) for i in range(20)])

print(random.sample(range(1,25),10))

ll=[random.randrange(1,30,2) for i in range(20)]
from collections import Counter
print([*Counter(ll)])
s='lakshmi Narayana Reddy Dwarampudi'
print("".join(sorted(set(s),key=s.index)))


# problem statement find the longest common prefix of Strings
def longestCommonPrefix(strs):
    size = len(strs)
    if (size == 0):
        return ""
    if (size == 1):
        return strs[0]
    strs.sort()
    end=min(len(strs[0]),len(strs[size-1]))
    i = 0
    while (i < end and
           strs[0][i] == strs[size - 1][i]):
        i += 1
    return strs[0][0: i]

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(longestCommonPrefix(["ll", "llllll", "lll", "lll", "lll"]))

def longestCommonPrefixFor(arr):
    result = arr[0]
    length = len(result)
    for i in range(1, len(arr)):
        while arr[i].find(result) != 0:
            result = result[:length - 1]
            length -= 1
            # Check for an empty case and return if true
            if not result:
                return "-1"

    return result
print(longestCommonPrefixFor(["ab", "cd", "abef", "gh", "ij"]))

ss=[ "cd", "abef", "abc","gh", "ij",'abcde']
ss.sort()
ss=sorted(ss,key=len)
result=""
for i in range(0,len(ss)):
    compareString=ss[i]
    for j in range(i+1,len(ss)):
        if ss[j].find(compareString)==0:
           result=compareString

print(result,"is the longest common prefix")
target=""
for item,value in Counter(s).items():
      target=target+"".join(item+value.__str__())
print(target)
from itertools import groupby
print("_____________________________",[(len(list(n)), m) for m,n in groupby(s)])

# from itertools import groupby
# s = 'aabbccccaa'
# print(''.join(k + str(sum(1 for x in g)) for k, g in groupby(s)))

source="Lakshmi Narayana Reddy Dwarampudi"
freeqDict={}
for i in source:
    if i in freeqDict:
        freeqDict[i]+=1;
    else:
        freeqDict[i]=1;
target=""
for key,value in freeqDict.items():
     target+=key+value.__str__()

print(target)


#Check if one string is a rotation of another.

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in (s2 + s2)

print(is_rotation("abcde","cdeab"))

print("abcde" in "cdeab"+"cdeab")

#rotate string to left

def rotateToLeft(s1,positions):
    positions = positions%len(s1)
    return s1[positions:]+s1[:positions]
print(rotateToLeft("ramesh",10))

#rotate string to right

def rotateToRight(s1,positions):
    positions = positions%len(s1)
    return s1[:positions]+s1[positions:]
print(rotateToLeft("ramesh",9))
s="long lon ago ther aee long smiles of words"
print(''.join(sorted(set(s),key=s.index)))


