# 자판기 시스템 #


title = """

=================================================================================================




신 장 개 업      맛 좋 은 찻 집 !




=================================================================================================
"""
print (title)






menu = {"쌍화차" : 500, "둥글레차" : 700, "레몬차" : 1000, "녹차" : 300}

print ("금액을 투입하세요")

money = int(input("\ : "))
ment = "원이 투입 되었습니다"
money = str(money)
print (money+ment)

"--------------------------------------------------------------------------------" # 입금 단계#

print(menu)

while True:
    tea = str(input("무슨 차로 드릴까요 ?"))


    if tea not in menu:
        print ( "메뉴에 없습니다. 다시 골라 주세요" )
    
    else:
        cup = int(input("몇잔 드릴까요 ?"))
        price = menu[tea] * cup
        money = int(money)
        if price <= money:
            print(str(price)+"원 입니다")
            change = money - price
            print ("여기 주문하신 %s와 잔돈 %s 원 입니다. 감사합니다." %(tea, change))
            break
        else:
            question = str(input("요금이 부족합니다. 추가요금을 내시겠습니까 ? : yes  or  no 로만 대답해주세요"))
            if question == "yes":
                A = price - money
                print ("현재 부족한 돈은 %s원입니다. 손님" %A)
                extra = int(input("금액을 투입하세요: "))
                B = (extra + money)
                change2 = B - price
                if  B >= price:
                    
                    print ("여기 주문하신 %s와 잔돈 %s 원 입니다. 감사합니다." %(tea, change2))
                    break
                elif change2 <= 0 :
                    C = money + extra
                    print ("부족합니다. 받은 %s원은 돌려드리겠습니다. 안녕히가세요." %C)
                                   
                    break

            else:
                print (f"받은 {money}는 돌려드리겠습니다. 안녕히가세요.")
                break
            
            
            
           
            
            
      
 



       
    






        



