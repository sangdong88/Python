# 앞의 문제들 중 비슷한 알고리즘이 있던 것 같지만, 같은 건 없다고 생각해서 올립니다. 
# 문제를 푸는데 많은 approach가 있을 듯 싶습니다. 
# 이 문제의 핵심은 비트 연산을 얼마나 잘 이해하고 있냐이기 때문에 비트 연산으로 풀어주세요.

# input은 int n을 입력 받아 첫번째 row는(n-1)의 O와 X, 두번째 row는(n-2)의 O와 XX, 세번째 row는(n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.

# 입력 예시: 6

# 출력 예시:

# OOOOOX

# OOOOXX

# OOOXXX

# OOXXXX

# OXXXXX

# XXXXXX

# 나의 답변

a = int(input("숫자를 입력하시오 :     "))
for i in range(1, a+1):
    print((6-i) * "O" + (i) * "X")




# best  
print((lambda n: '\n'.join('O'*(n-i) + 'X'*i for i in range(1,n+1)))     (int(input('>>>'))))

# lambda 함수 는

# 람다의 정의는 간단합니다.



# lambda 인자리스트: 표현식



# >>> g = lambda x: x**2

# >>> print(g(8))

# 64

# >>>

# >>> f = lambda x, y: x + y

# >>> print(f(4, 4))

# 8

# >>>



# 람다 정의에는 "return"문이 포함되어 있지 않습니다. 반환값을 만드는 표현식이 있습니다. 함수가 사용될 수 있는 곳에는 어디라도 람다 정의를 넣을 수 있으며, 위의 예 처럼 변수에 할당하여 사용할 필요는 없습니다.





# 다음은 람다 함수의 사용법을 보여줍니다.



# >>> def inc(n):

# 	return lambda x: x + n



# >>> f = inc(2)

# >>> g = inc(4)

# >>> print(f(12))

# 14

# >>> print(g(12))

# 16

# >>> print(inc(2)(12))

# 14

# >>> 



# 위의 코드는 inc 함수로 lambda 함수를 즉석에서 생성하고 반환 하는 함수를 정의 합니다. 리턴 된 함수는 인수를 작성시 지정된 값만큼 증가시킵니다.



# 이제 여러 개의 서로 다른 증분 함수를 만들어 변수에 할당 한 다음 서로 독립적으로 사용할 수 있습니다. 마지막 문장에서 알 수 있듯이 lambda 함수를 어떤 변수에 할당할 필요조차 없습니다. 즉각적으로 사용할 수 있고 더 이상 필요하지 않을 때 잊어 버릴 수 있습니다.




# 1. map() 함수



# 람다 함수의 장점은 map() 함수와 함께 사용될 때 볼 수 있습니다.  map() 은 두 개의 인수를 가지는 함수입니다.



# r = map(function, iterable, ...)



# 첫 번째 인자 function 는 함수의 이름 입니다. 두 번째 인자 iterable은 한번에 하나의 멤버를 반환할 수 있는 객체 입니다.(list, str, tuple) map() 함수는 function을 iterable의 모든 요소에 대해 적용합니다. 그리고 function에 의해 변경된  iterator를 반환합니다.



# >>> a = [1,2,3,4]

# >>> b = [17,12,11,10]

# >>> list(map(lambda x, y:x+y, a,b))

# [18, 14, 14, 14]



# 2. filter() 함수



# filter() 함수도 두 개의 인자를 가집니다.



# r = filter(function, iterable)



# filter에 인자로 사용되는 function은 처리되는 각각의 요소에 대해 Boolean 값을 반환합니다. True를 반환하면 그 요소는 남게 되고, False 를 반환하면 그 요소는 제거 됩니다.



# >>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# >>> list( filter(lambda x: x % 3 == 0, foo) )

# [18, 9, 24, 12, 27]



# 3. reduce() 함수



# reduce() 함수를 두 개의 필수 인자와 하나의 옵션 인자를 가지는데, function 을 사용해서 iterable을 하나의 값으로 줄입니다. initializer 는 주어지면 첫 번째 인자로 추가 된다고 생각하면 됩니다.



# functools.reduce(function, iterable[, initializer])



# 예를 들어 reduce(function, [1,2,3,4,5]) 에서 list 는 [function(1,2),3,4,5] 로 하나의 요소가 줄고, 요소가 하나가 남을 때까지 reduce(function, [function(1,2),3,4,5]) 를 반복합니다.



# >>> from functools import reduce

# >>> reduce(lambda x,y: x+y, [1,2,3,4,5])

# 15



# 위에서 map()과 filter() 는 내장 함수이고, reduce() 는 아닙니다.

 

