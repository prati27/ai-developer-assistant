class Document:
    def __init__(self,title,content,author):
        self.title=title
        self.content=content
        self.author=author

    def show_summary(self):
        print(f"Title: {self.title} | Content: {self.content} | Author: {self.author}")

