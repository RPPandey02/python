# try:
#     a=int(input("en-"))
#     print(100/a)
# except Exception as e:
#     print("problem is ",e)
# except FileNotFoundError as fl:
#     print(fl)
# else:
#     print("this block happen when nn error is found ")
# finally :
#     print("done")

# it work anywhere, even in function 

# def intr():
#     try :
#         a=int(input("enter- "))
#         print(a)
#     except:
#         print("your is not right")
#         intr()
# intr()

def intr():
    a=int(input("enter- "))
    if a<0:
        raise Exception("you have negative no. ",a)
    # we can use different expection or error and raise it
    
    else:
        print(a)
intr()

