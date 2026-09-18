# topics covered :

## 1. tuples:
Starts with () , whereas list starts with [].

A tuple is a collection of values just like list.

The main difference:

List [] → can be changed
Tuple () → generally cannot be changed

we need tuple when we dont want some part of the program to accidentally change the collection. in list the change can happen but not in tuple.

## 2.Sets:
Set is a collection that only store unique values
no duplicate allowed 
starts with {}
no key value pair like dictionary.

useful in real world application to remove duplicates from collections.

No order — unlike lists/tuples, sets don't guarantee any particular order, so you can't access items by index (tags[0] doesn't work on a set)
No duplicates — the core feature
Add with .add(), not .append():

## 3. classes & objects

we need a class because every document need to have a behaviour of its own while storing data ,which is not possible in case of dictonary , 
so we use classes 

A class can do both , can store as well as have some behaviour of its own.

class is just a blueprint , nothing but a template which is not real .

whereas an object is a real thing built from a blueprint.
so we will be having different obejcts from same class


example:
class House:
house1 = House()
house1 = House()

class Document:
    pass //means class Documents is empty for now , only the class exists.when we have to do nothing after indentation just write pass to avoid error

class Document:
    pass
doc1= Document()
print(doc1)


## 4.Initialiser (--init--)
this we will use to set data in one line rather than manually writing it in repetive manner

__init__ runs automatically when you create an object and initializes its attributes with the values you provide.

example:
class Document:
    pass
doc1= Document()
doc1.title="Pyhon Heor"

doc2 = Document()
doc2.title="Java for beginners"

print(doc1.title)
print(doc2.title)

like here how we have to set data and value in the object everytime so to avoid that we will use --init--

## instead of manually attaching data after creating the object, you set up the class so the data gets filled in automatically, right when the object is created.


def __init__(self, title, content): 
//special function whose name is always init.
Python looks for this specific name and runs it automatically the instant you create a new object.

# self refers to the current object that the method is operating on.

    self.title = title
    self.content = content


 ## methods

 A method is just a function that lives inside a class and belongs to its objects.
A method lets you package that into something reusable, attached to the object itself.


example:

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

Document("Python Basics", "Learning loops.")
        │
        ▼
Step A: Python creates a blank object → {} (nothing on it)
        │
        ▼
Step B: Python calls __init__(self=blank_object, title="Python Basics", content="Learning loops.")
        │
        ▼
Step C: Inside __init__: self.title = "Python Basics"  → object now has title
        │
        ▼
Step D: self.content = "Learning loops."  → object now has content
        │
        ▼
Step E: the now-filled object gets returned and stored in doc1

# output:
Calling on doc1:
self is currently: Python Basics
Python Basics: Learning loops.
Calling on doc2:
self is currently: Java Basics
Java Basics: Learning classes.


✅ class = blueprint
✅ object = a real thing built from that blueprint
✅ __init__ = automatic setup when object is created
✅ self = automatically-supplied reference to "this object"
✅ methods = functions that belong to a class, work off self


-----------------------------------

# 5 .Inheritance:
sometimes you want a new class that's mostly like an existing class, but with a few extra things added. 
Instead of rewriting everything from scratch, you can have one class inherit from another — reusing its __init__ and methods automatically.


example:

class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def show_summary(self):
        print(f"{self.title}: {self.content}")


class PDFDocument(Document):   
    def __init__(self, title, content, page_count):
        super().__init__(title, content)   # reuse Document's __init__
        self.page_count = page_count

    def show_pages(self):
        print(f"This PDF has {self.page_count} pages")


- class PDFDocument(Document):   class PDFDocument(Document): → the (Document) part means "PDFDocument inherits everything from Document." - PDFDocument is called the child class, Document is the parent class

-super().__init__(title, content) → this means "run the parent class's __init__ first, to set up title and content the same way Document already does" — instead of rewriting self.title = title again yourself.

-self.page_count = page_count → then you add the extra thing specific to PDFDocument — something a plain Document doesn't have.  

----------------------------------

## 6.FilePath

A filepath tell your computer where file is located

- Relative path — starts from where your program/project is working

- Absolute path — gives the complete location on your computer,

# Your assistant will eventually need to find and read files containing knowledge.

-------------------------------------


# 7.Reading a file 

python uses open() for this

Mode	Meaning
"r"	    Read
"w"	    Write
"a"	    Append


# better way to write the code is below 
The with statement automatically closes the file for us, even if something goes wrong.

after the with line the file close automatically we dnt need to write file.close()
------------------------------------------

# 8.writing a file
"w" → opens the file in write mode
.write() → writes the supplied string/text into the file

with open(file_path, "w") as file:
    file.write("Hello from Python!")


    it overwrittes on the exisiting content of the file 

# 9. Append a file

with open("notes/test.txt", "a") as file:
    file.write("\nPython") 
    adds the text after the exisiting one


# 