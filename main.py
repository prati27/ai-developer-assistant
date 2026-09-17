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

name = input("Enter your name: ")
favourite_language = input("Enter your favourite programming language: ")
print("Hello, " + name + "! Your favourite programming language is: " + favourite_language)

print(f"Whats yours name ? {name}")
print(f"Whats your favourite language ? {favourite_language}")


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