#def gugu(a):
#    for i in range(1,10):
#        print(f"{a} X {i} = {a*i}")
#gugu(4)


def gugu(*a):
    for j in range (len(a)):
        print('\n')
        #print(j) #a 의 갯수가 3이기 때문에 j는 0 , 1, 2 
        for i in range (1,10):
            print(f'{a[j]} X {i} = {a[j]*i}',end = ' ',)

gugu (2,3,4)