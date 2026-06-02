# # import greet
# # import pymath
# # greet.greeting("python")

# # pymath.sum(1,2)
# # greet.greeting(pymath.person1['name'])
# # #ceil function for finding next round off number 
# # n=7 
# # n=5 
# # print(math.comb(n,k))
# #print(math.factorial(9))
# #print(math.trun(2.75))- uska decimal part remove kardega or sirf integer part dega 
# #print(math.remainder)- modulus ki tarah kaam karta hai 
# #print(math.pi)
# #print(math.tau)
# # import datetime
# # date = "2-6-2026"
# # x= datetime.datetime.now()
# # print(x)
# # print(x.year)
# # print(x.month)
# # print(x.day)

# import datetime
# # date = "2-6-2026"
# x= datetime.datetime.now(2026,6,2)
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)

import random
cnum = random.randrange(0,50)
print(cnum)
unum = int(input("enter your number :"))
if cnum>unum:
    print("computer numbr",cnum,"is greater")
elif unum>cnum:
    print("computer numbr",cnum,"is smaller") 
else :
    print("computer numbr",cnum,"is small")    