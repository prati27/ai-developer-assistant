from document import Document  #document name of the file , Document is the class

doc1 = Document("Python Basics", "Learning loops.", "Alex")
doc2 = Document("Java Basics", "Learning classes.", "Pratikshya")

doc1.show_summary()
doc2.show_summary()


from document import Document
from document_manager import DocumentManager

manager = DocumentManager() #object manager created which keeps track of multiple doc
print(manager.documents)

doc1 = Document("Python Basics", "Learning loops.", "Alex")
doc2 = Document("Java Basics", "Learning classes.", "Pratikshya")

manager.add_document(doc1)
manager.add_document(doc2)

manager.list_documents()