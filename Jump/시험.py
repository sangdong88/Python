# 시험 번호

A = {1:98, 2:78, 3:56, 4:68, 5:89, 6:23, 7:58, 8:90, 9:100, 10:57}

while True:
    key = int(input("수험 번호를 입력 하세요:"))
    if key in A:
        value=A.get(key)
        if value > 70 :
            print ("합격")
            break
        else:
            print ("불합격")

    else :
        print ("수험번호를 확인하세요")
     
