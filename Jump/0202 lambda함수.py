#def func(a):
 #   I=[]
  #  for i in range (a):
   #     I.append(i**2)
    #return I
#print(func(5))

print(list(map((lambda a: a**2),range(5))))
