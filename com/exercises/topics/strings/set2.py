#Given the string "The quick brown fox", slice it to print "The brown fox"

str="The quick brown fox"
print(str[:str.find("quick")]+str[str.find("quick")+len("quick")+1:])

#Given the string "abcdefgh", slice it to print "gfe".

str="abcdefgh"
print(str[-2:-5:-1])

#Given the string "OpenAI", slice it to print "Open".
text = "OpenAI"
print(text[:4])
#text = "Welcome to Python Programming"  slice it to print "Python Programming".
txt = "Welcome to Python Programming"
print(txt.find("Python"),len(txt))
print(txt[txt.find("Python"):len(txt)])

# Given the string "12345", slice it to print "234".
string="12345"
print(string[1:-1])
print(string[1:4])

#Given the string "Mississippi", slice it to print "ssissi".

string="Mississippi"
print(string[2:8])

#String Formatting:
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")