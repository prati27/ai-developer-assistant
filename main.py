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

#try:
 #   age = input("Enter your age: ")
#    age = int(age)
 #   print(f"Next year you'll be {age + 1}")
#except ValueError:
#    print("Please enter digits only, like 25, not words like 'twenty'")
    #you can prevent it from crashing your whole program:

document_types = ("pdf", "txt", "docx")

print(document_types) #("pdf","txt","docx")
print(document_types[0]) #pdf

supported_types = ("pdf", "txt", "docx")

print(supported_types)
print(supported_types[1])
print(type(supported_types))

tag={"stage","commit","push","init"}
print(tag)
tags={"stage","commit","push","init","commit"} #duplicate added so set remove duplicate automatically while printing
print(tags)

tags = {"python", "ai"}
tags.add("backend")
print(tags)

tags = ["python", "ai", "python", "llm", "ai", "backend"]

unique_tags = set(tags)
print(unique_tags)
print(len(unique_tags))
print(type(unique_tags))

# List — ordered, changeable, duplicates OK
documents = ["pdf", "txt", "pdf"]
documents[0] = "docx"          # ✅ allowed
print(documents)                # ['docx', 'txt', 'pdf']

# Tuple — ordered, LOCKED, duplicates OK
supported_types = ("pdf", "txt", "pdf")
#supported_types[0] = "docx"    # ❌ error — can't change

# Dictionary — labeled data (key → value)
document = {"title": "Python Basics", "pages": 20}
print(document["title"])       # access by key, not position

# Set — unique values only, no order, no duplicates
tags = {"python", "ai", "python"}
print(tags)                     # {'python', 'ai'} — duplicate auto-removed


#classes and objects:
class Document:
    pass

doc1 = Document()
print(doc1) # <__main__.Document object at 0x000001F0FA9B6900> this is saying python's default way of saying here the document object and this is the memory addresst.


class Document:#class declared
    pass

doc1 = Document() #object created
doc1.title = "Python Basics" #manually add data to object
doc1.content = "Learning loops."

print(doc1.title)
print(doc1.content)

#What's happening: doc1.title = "Python Basics" attaches a piece of data called title directly onto the doc1 object — no constructor needed at all. doc1.content = ... does the same for content. Then you read them back with doc1.title / doc1.content.

#so this creates a title data inside object and gives it the value via this. similary with contnet as well

class Document:
    pass
doc1= Document()
doc1.title="Pyhon Heor"

doc2 = Document()
doc2.title="Java for beginners"

print(doc1.title)
print(doc2.title)


# here two objects are created from same class with different title value stores in it manually


#initialiser (--init--)

class Document:
    def __init__(self,title,content):
        self.title=title
        self.content=content

doc1 = Document("Python Basics","LEarning loops")
print(doc1.title)
print(doc1.content)


class Document:
    def __init__(self,title,content):
        self.title=title
        self.content=content
doc1=Document("Python basics","Loops")
doc2=Document("Java","Constructor")

print(doc1.title)
print(doc1.content)
print(doc2.title)
print(doc2.content)


class Document: ##this class has two methods one init and other show summmary
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def show_summary(self):
        print("self is currently:", self.title)
        print(f"{self.title}: {self.content}")

doc1 = Document("Python Basics", "Learning loops.") #objects created
doc2 = Document("Java Basics", "Learning classes.")

print("Calling on doc1:")
doc1.show_summary()

print("Calling on doc2:")
doc2.show_summary()


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def show_info(self):
        print(f"Book {self.title}: by {self.author}")
book1 =Book("Malgudi Tales","Ruskin Bond")
book2 = Book("Romeo juliet","William shakesphere")

print("Loading info for book 1")
book1.show_info()

print("Loading info for book 2")
book2.show_info()


class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def show_info(self):
        print(f"Brand :{self.brand},Model:{self.model}")

class Car(Vehicle):

    def __init__(self,brand,model,doors):
        super().__init__(brand,model)
        self.doors=doors

    def show_doors(self):
        print(f"This car has {self.doors} doors")

car=Car("Toyota", "Corolla",4)
car.show_info()
car.show_doors()

class Document:

    def __init__(self,title,content):
        self.title=title
        self.content=content

    def show_summary(self):
        print(f"{self.title}: {self.content}")

doc = Document("Java for beginners","Charles")
doc.show_summary()

file_path = "notes/day02.md"
print(file_path)

file_path = "notes/day02.md"
file = open(file_path, "r") #file_path which tell python which file , r means read mode
content = file.read() #stores the content of the file in content
print(content) #print that stored in content which is in day02.md
file.close() #closes the file after finishing the task


#better way to write the code 
#The with statement automatically closes the file for us, even if something goes wrong.

with open(file_path, "r") as file:
    content = file.read()

print(content)

## file means opened file 
## content is the text inside that file

## with is prefereed as after the with line it automatically closes that file irrespective of error so we dont need to write the file.close() again

# writing a file
file_path="notes/text.txt"

with open(file_path,"w") as file:
    file.write("Hello from pythhon")
      
print("Done")


open("notes/text.txt", "r")
open("notes/text.txt", "w")
open("notes/text.txt", "a")
    
