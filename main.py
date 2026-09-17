print("AI knowledge Assistant")
print("Welcome to my AI learning journey!")

project_name= "AI Knowledge Assistant"
name="Pratikshya Nayak"
age="26"
goal="To learn and explore the possibilities of using AI in our current work , to build agents to ease the workload"
print(project_name)
print(name)
print(age)
print(goal)

project_name = "AI Knowledge Assistant"
document_count = 5
temperature = 0.7
assistant_enabled = True

print(type(project_name))
print(type(document_count))
print(type(temperature))
print(type(assistant_enabled))

#name = input("Enter your name: ")
#favourite_language = input("Enter your favourite programming language: ")
#print("Hello, " + name + "! Your favourite programming language is: " + favourite_language)

#print(f"Whats yours name ? {name}")
#print(f"Whats your favourite language ? {favourite_language}")


total_document=20
documents_added_today=3
total_documents_till_date=total_document+documents_added_today
print("Total documents till date: " + str(total_documents_till_date))
print("Average documents added per day:"+str(documents_added_today/1))

print(f"Total documents till date : {total_documents_till_date}")
print(f"Average documents added per day :{documents_added_today/1}")

document_count = 2
if document_count == 0:
    print("No document yet")
elif document_count >=1 and document_count <=4 :
    print("You have a few documents")
else :
    print("You have many documents")

for i in range(1,6):
    print(f"Document {i}")

count = 0
while count<=3:
    print(f"Processing documents {count}")
    count =count+1  #count +=1

doc =["Spring boot","Python","RAG overview"]
print(len(doc))
doc.append("Langchain")

for i in range(1,len(doc)+1):
    print(f"{i}.{doc[i-1]}") ##here it prints the value stored in it  and fetchs the value from the index positon

document = {
    "title": "Python Basics",
    "author": "your name",
    "pages": 20,
    "is_published": True,
    "topics": ["variables", "loops", "functions"]
}

print(document)
print(document["title"])
print(document["topics"])
print(type(document))
print(type(document["topics"]))    

document ={
    "title":"Java for beginners",
    "author":"Prayikshya",
    "pages":100,
    "topic":["BAsics","String","loops"]
}

print(document)
print(document["title"])
print(document["author"])

for key,value in document.items():
    print(key,":",value) 

for key in document.keys():
    print(key)

for value in document.values():
    print(value)

def greet(name):
    print(f"Hello,{name}")

greet("Alex")
greet("Pratikshya")

def add_num(a,b):
    result=a+b
    return result
total=add_num(5,3)
print(total) 
#here the return sends the value to total when the function add_num with paramters(5 and 3)are called the return result is stored in total and printed

#in python we dont declare the data types in the parameters

def add_documents(count1,count2):
    result = count1+count2
    return result

total=add_documents(2,4)
print(total)

def add_documents(count1,count2):
    total = count1+count2
    return total
result1 = add_documents(5, 3)
print(result1) #return total saves the value and store in result 1

result2 = add_documents(10, 20)
print(result2)
# here also tottal returns the value after adding and stores in the result 2

def describe_document(title, pages=0): ##page has a fallback or default value which is used when we dont provide any value for the page paramter
    print(f"Title: {title}, Pages: {pages}")

describe_document("Python Basics", 20)
describe_document("Java Basics")


title = "   Python Basics for AI   "
print(title.strip())
print(title.lower())
print("AI" in title)
tags = "python,ai,backend,rag"
print(tags.split(","))


age = input("Enter your age: ")
age = int(age)
print(f"Next year you'll be {age + 1}")

#Enter your age: twenty
#Traceback (most recent call last):
#  File "F:\ai-knowledge-assistant\main.py", line 145, in <module>
#    age = int(age)
#ValueError: invalid literal for int() with base 10: 'twenty'
#so here int doesnt know how to convert twenty into a number so it crashes

try:
    age = input("Enter your age: ")
    age = int(age)
    print(f"Next year you'll be {age + 1}")
except ValueError:
    print("Please enter digits only, like 25, not words like 'twenty'")
    #you can prevent it from crashing your whole program: