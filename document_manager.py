class DocumentManager:
    def __init__(self): #keep list of documents
        self.documents=[] # documents =[] is a empty list assigned to variable document
        # self points or refers to specific object currently being worked on than routing somewhere else
        #we use self as we want this to belong to particular object
    
    def add_document(self,document):
        self.documents.append(document)

    def list_documents(self):
        for document in self.documents:
            document.show_summary()