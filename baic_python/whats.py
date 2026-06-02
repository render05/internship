# import pywhatkit

# pywhatkit.sendwhatmsg("+917357351578","hi",10,52)



import random
choices =['rock','paper','scissor']
uscore=0
coscore=0
# char = User
# char = comp
i=1
while i<=5 : #loop runs until 6 then compares 
  user = input("enter from 3:")
  comp = random.choice(choices)
  print("user chose:",user)
  print("computer chose:",comp)



  if(user=="scissor" and comp=="paper") or \
   (user=="rock" and comp == "scissor") or \
   (user=="paper" and comp == "rock"):
    uscore=uscore+1
    print("user wins this round")
  elif(user=="rock" and comp=="paper") or \
     (user=="paper" and comp == "scissor")or \
     (user=="scissor" and comp == "rock"):
      coscore=coscore+1
      print("comp wins this round")
  else:
     print("match draws")
  i=i+1
print("\nfinal scores")
print("user score:",uscore)
print("comp score:",coscore)





if(uscore>coscore):
  print("user won")
elif(coscore>uscore):
  print("comp won")
else:
  print("game draw")
 









