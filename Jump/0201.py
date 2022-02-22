import sys
f = open("b.txt","w")
sys.stdout = f

for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))
        

f.close()


import os
os.mkdir('D:\코딩\Desktop\python')

