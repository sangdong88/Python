# a = input ("숫자를 입력 하세요 :     ") # 예 2,3,4,5
# print(a, type(a)) 
# print(a[0::2]) # 여기까지 str
# a1 = list(a[0::2]) # 리스트로 만들어
# print(type(a1),a1) # 리스트 안에 객체 1개씩 ['2','3','4','5']

# b = range(0,10)
# print(b, type(b))

def ave(*args):
    result = 0
    for i in args :
        result += i
        print(result, type(result))
    return result / len(args)



print(ave(4,2,3,4,2), type(ave(4,2,3,4,2)))