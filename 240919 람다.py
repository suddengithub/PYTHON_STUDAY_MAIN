# 람다란? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 파이썬에서는 람다 함수를 통해서 이름 없는 함수를 만들 수 있음
# 함수와 람다 비교
def add(a, b):
    return a + b

print(add(10, 20))
print((lambda a, b: a + b)(10,20))

def power(n):
    return n * n

# square = lambda x: x * x # square는 함수 이름이 아니라 변수

in_val = [1,2,3,4,5,6,7,8,9,10]
pow_val = list(map(lambda x: x * x, in_val)) # 람다를 이렇게 입력하는것은 함수값이기 때문에, 한번 쓰고 버릴거기 떄문
print(pow_val)











