#file handling is doneby various funcs.
#E:\vscode\python\file handling\text.txt "E:\vscode\python\file handling\text.txt"
#file for editing

# ope a file for edit

f= open("e:\\vscode\\python\\file handling\\text.txt",mode="r+")
# mode=" ", we put to do edits
    # r: open an existing file for a read operation.
    # w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
    # a:  open an existing file for append operation. It won’t override existing data.
    # r+:  To read and write data into the file. The previous data in the file will be overridden.
    # w+: To write and read data. It will override existing data.
    # a+: To append and read data from the file. It won’t override existing data.

# to read a file complete from cursor
print(f.read(), end="\n\n")

# to tell where cursor is 
print(f.tell(), end="\n\n")

#to set cursor , at '0'
print(f.seek(0))

#towrite the in file 
f.write("this is the new line that i entered")

# readline() gives single line from cursor 
print(f.readline())

#l is a list where lines are saved 
l=f.readlines()

# close the file and finsh its editing 
f.close()