project_name="AI for beginners"
total_documents = 300
avg_rating =30.0
is_active = False

name = input("Whats is your name")
doc_title=input("what title would you like to add")

print(f"welcome {name } to the {project_name}")

list=["AI token","AI security","ai scaling"]
list.append("AI vs humans")
print(len(list))

document ={
    "title":"Python hero",
    "author":"John roboot",
    "pages":30,
    "tags":["Python","tool calling","LLM"]

}

for key,value in document.items():
    print(key,":",value)

def describe_document(title,pages=0):
    return (f"Title: {title}, Pages: {pages}")

result = describe_document("Python for beginners")
print(result)

total_documents = 20
if(total_documents == 0):
    print("No Documents yet")
elif(total_documents>1 and total_documents<4):
    print("A few documents")
else:
    print("Many documents")

for i in range(len(list)):
    print(f"{i}.{list[i]}")



print(doc_title.upper())
print(doc_title.strip())
print("AI" in doc_title)

try:
    pages=input("Enter number of pages ? ")
    page=int(pages)
    print(f"the number of pages are {page}")
except ValueError:
        print("Please enter proper number of page instead of String")



