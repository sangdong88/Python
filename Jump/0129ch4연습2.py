

def ave(*inp):
    result = 0
    for i in inp :
        result += i
        print(result, type(result))
    return result / len(inp)



print(ave(4,2,3,5), type(ave(4,2,3,5)))
