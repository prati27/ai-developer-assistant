# Day1 :
 topics covered:
 -concepts of python 
 1.print()
 2.variable
 3.data type
 4.input from user input()
 5.operations and basic calculation
 6.f-strings
 7.if,elif,else
 8.loops
 9.lists




 # details flow:
 # 1 . print()- 
 in python is this print statement , used for displaying on screen .

 example: print("ABC") - the text inside the method is a string ,which gets printed.

 # 2.variables in python: 
 a name which has some data referred to it.

if name="String" :
 where name is the variable to which  "String" is assigned.

 # 3.Data types:
 A variable can have different type of data , the type of data which it contains and hence this is called data type.

like String - str is a string data type 
so name = "Pratikshya nayak " here name is of string data type 

age= 26 , here age is of integer /int data type .

# so in python the type() method determines the type of the variable 
example - name="Pratikshya"
type(name) = str 

---------------------------------
# so if document_count = 5
python understand it as 
variable - document_count
5 - value
int - data type

----------------------------------

# 4.Input from user:

name ="Pratikshya" this is a hardcoded value ,

# so to fetch input from user we use input()
Example:
name=input("What is your name ?")
print("Hello")
print(name)

here we are storing the name of the user we recieved in the name variable via input() and printing it using print().

---------------------------------------------------

# 5.Operators & Basic calculations :
python helps to do the calculations with the variables itself.

Example:

total_documents = 10
documents_read = 4

documents_remaining = total_documents - documents_read

print(documents_remaining)=6

## also one thing '+' this sign only concates same type of data types like str+str or float+float

-------------------------------------------------

# 6. f-strings (a cleaner way to print)

A f-string is a cleaner approach to print anything in python rather than writing big synatx lines with '+' and adding number of variables , so avoid the messier code we us f-strings

in this we add f to the beginning of the string anf drop the variable inside the {}.

Example:
print("Total documents till date: " + str(total_documents_till_date))

this can be written as :
print(f"Total documents till date :{total_documents_till_date}")

# No +, no str() — Python automatically converts whatever's inside {} into text for you, no matter if it's an int, float, or bool.

----------------------------------------------------

# 7.Conditonal Statements:(if/elif/else)

this lets program run decisions based on the code whether something is true or false.

# importance
Why this matters for my project: 
Soon you'll write things like "if this document title already exists, don't add it again" or "if the user's search query matches a document, show it." That's all if/else under the hood.

## learnings : in python it needs to be intendend else it will throw error and also && operator is not valid in python it used 'and' also they use 'or' inplace of '||'.

------------------------------------------------------------

## 8.Loops(for and while)

helps us repeat the action until conditon runs out instead of letting us write the same task again and again

example:
# for loop 
for i in range(5):
print(i)

meaning: i is the variable name that hold current value each time.
and in means it has to go through
range (5) means {0,1,2,3,4}

## need of fpr loop in our project : once you have a list of documents, you'll use a for loop to go through each one — e.g. print every document's title, or search through all of them for a keyword.

# while loop
runs till condition is true

count =0
while count<=5:
print(count)
count = count+1 or  count +=1

## Important: you must change the variable (count) inside the loop, or it'll run forever (an "infinite loop") — a very common beginner mistake.

----------------------------------------------------

## 9.Lists

a list id a way to store multiple values in an order , in a single variable
doc =["Spring","Java","Python"]
index starts from 0

to access items we can write
print(doc[0]) - Spring
print(doc[1]) - Java
etc..

## common list operations
documents = ["Spring Boot Architecture", "Python Basics"]

# adds an item to the end
documents.append("RAG Overview")    

print(documents)                      
# ['Spring Boot Architecture', 'Python Basics', 'RAG Overview']

# removes a specific item
documents.remove("Python Basics")  

print(documents)                      
# ['Spring Boot Architecture', 'RAG Overview']

# 2 — number of items in the list
print(len(documents))                 


------------------------------
## 10.Dictionaries
A python dictionary groups the diff info together.

In a variable also we store the values but for example 
name="Python"
pages=20
author="John"

these are three diff info which needs to be stored inn one document orelse needs to be stored together thats what dictionaries is for.


Syntax :
document = {
    "title":"Python Basics",
    "pages":20,
    "author":"John"

}
print(document)
## output : {'title': 'Python Basics', 'pages': 20, 'author': 'John'}

-dictionary is a key-value pair

key       → value
-------------------------
"title"   → "Python Basics"
"pages"   → 20
"author"  → "John"

- to get a value of a particular key we can write:
print(document["title"]) - Python Basics

## example 2:
document = {"title": "Spring Boot Architecture", "author": "Alex"}

# print(document["title"])          
Spring Boot Architecture

# document["author"] = "Pratikshya"  
 change a value

# print(document["author"])          
Pratikshya

document["pages"] = 20             
# add a brand new key

print(document)

## why dicitonary matter for AI projects :

- JSON is simply a standard text format for representing data.

- JSON (JavaScript Object Notation) is the standard format almost every API, LLM response, and config file uses to send/receive data over the internet. 

Python dictionaries and JSON look nearly identical.
 
 A Python dictionary is a Python data structure.
JSON is a text/data interchange format.

In dictionary , while running the for loop we use .items() which gives us key-value pair , one at a time.

----------------------------------------
## 11. Functions(def)

a reusable piece of code , which cn be used to run wherever necessary instead of writing multiple times .

def - keyword that starts a function definition

defining a function doesn't run it.
 Nothing happens until you call it — say_hello() on the last line is what actually executes it.

example :
def say_hello:
(
    print("hello")
)
say_hello() //calling the function


## function with input parameters :
def greet(name):
print(f"Hello,{name}")

greet("Alex")
greet("Pratikshya")

//here the function greet takes name as the input paramter 

output: 
Hello, Alex
Hello, Pratikshya

## function which give back a result(has a return statement)

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total) - 8

## imp 
In a paramterised function when we dont add any value to the parameter while calling the function it crashes so its always good to give defaults paramter value /fallback value.

----------------------------------------------

# 12. String methods:
Strings come with built-in functions (methods) for cleaning, searching, and transforming text.

1.lower()

2.upper()

3.strip()-removes extra space from start/end
useful when we accidentally add any input with trailing spaces

4.replace(old,new) - swap text

5.split(separator)-break string into a list
if a user types tags separated by commas, .split(",") turns that single string into a usable list.

6.in - checks if text contains something
helps in document title search.

---------------------------------

# 13. Error handling (try / except)
 A way to handle errors gracefully instead of letting your program crash.