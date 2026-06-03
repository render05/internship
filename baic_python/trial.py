# # # import greet
# # # import pymath
# # # greet.greeting("python")

# # # pymath.sum(1,2)
# # # greet.greeting(pymath.person1['name'])
# # # #ceil function for finding next round off number 
# # # n=7 
# # # n=5 
# # # print(math.comb(n,k))
# # #print(math.factorial(9))
# # #print(math.trun(2.75))- uska decimal part remove kardega or sirf integer part dega 
# # #print(math.remainder)- modulus ki tarah kaam karta hai 
# # #print(math.pi)
# # #print(math.tau)
# # # import datetime
# # # date = "2-6-2026"
# # # x= datetime.datetime.now()
# # # print(x)
# # # print(x.year)
# # # print(x.month)
# # # print(x.day)

# # import datetime
# # # date = "2-6-2026"
# # x= datetime.datetime.now(2026,6,2)
# # print(x)
# # print(x.year)
# # print(x.month)
# # print(x.day)

# import random
# cnum = random.randrange(0,50)
# print(cnum)
# unum = int(input("enter your number :"))
# if cnum>unum:
#     print("computer numbr",cnum,"is greater")
# elif unum>cnum:
#     print("computer numbr",cnum,"is smaller") 
# else :
#     print("computer numbr",cnum,"is small")    
# import os 
# os.chdir(r"C:\Users\shail\Desktop\my-project")
# i=1
# for file in os.listdir():
#     src = file 
#     dst = "assign"+str(i)+".txt"
#     os.rename(src,dst)
#     i+=1
#     print(file)
# pip intall qrcode
# import qrcode
# data ={
#     'url':'https:/www.coplur.com/home'
# # }
import qrcode
data = 'https://gemini.google.com/app/6d6515487c5340b4'
img = qrcode.make(data)
img.save('qrcode.png')


import cv2 
image = cv2.imread("qrcode.png")
detector = cv2.QRCodeDetector()
data,vertices_array,binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None and data:
    print(f"QR data:{data}")
else:
    print("no data found ")    