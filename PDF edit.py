#we can edit pdf or more using python
    # Extracting document information (title, author, …)
    # Splitting documents page by page
    # Merging documents page by page
    # Cropping pages
    # Merging multiple pages into a single page
    # Encrypting and decrypting PDF files
    # and more!
import PyPDF2
p=open("E:\\vscode\\python\\sample.pdf","rb")
preader=PyPDF2.PdfReader(p)
print(len(preader.pages))
page1=preader.pages[0]
print(page1.extract_text())
p.close()