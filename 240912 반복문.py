#조건이 참인 동안 반복 수행
# n = int(input("정수 입력 : "))
# sum = 0 # 값을 누적하는 변수. 반드시 초기값을 넣어줘야 한다.
# while n: # 0이 아닌 모든 값은 참으로 간주 (자바 제외) # 자바의 경우 조건식을 만들면, while n > 0:
#     sum += n # sum = sum + n
#     n -= 1 # n = n - 1 , n--
# print(sum)

# for i in range(1, n+1): # 범위 기반의 for문
#     sum += i
# print(sum)

# while문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용
# while True: # 반복문 내에 탈출 조건이 있어야 함
#     age = int(input("나이를 입력하세요 : "))
#     if 0 <= age <= 200: break # 정상적인 입력이므로 반복문 탈출 # break가 들어갔기 때문에 else는 넣어도 안 넣어도 됨. 어차피 위에서 빠져나감
#     print("나이를 잘 못 입력 하셨습니다.")
#
# print(f"당신의 나이는 {age}입니다.")

# for 문 : 정해진 범위 만큼을 반복 수행할 때 효과적
# for 요소 in 시퀀스: 시퀀스 자료에 대한 자동 순회,
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# name = "dskfjsfklsjfs"
# for e in name:
#     print(e, end="-")

# for e in input("문자열 입력 : "):
#     print(e, end="-")

# for 인덱스 in range(시작값, 종료값, 증감값):
# n = int(input("정수 값 입력 : "))
# sum = 0
# for i in range(n + 1): # 시작값이 0인 경우 생략 가능, 증감값이 1인 경우 생략 가능
#     sum += i
# print(sum)

# 이중 for문 사용하기
# n = int(input("정수 입력 : "))
# for i in range(n): # 0 ~ n 미만까지
#     print(f"i={i} ", end="")
#     for j in range(n):
#         print("*", end=" ")
#     print()

# 이중 for문 구구단 찍기
# for i in range(2, 10): # 2단에서 9단까지
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")
#     print("-"*20)

# 제어문 : break, continue
# break : 반복문을 탈출할 때 사용
# continue : 아래의 문장을 수행하지 않고 반복문의 조건식으로 이동,
# (해당 루틴은 수행된걸로 간주)
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue # 짝수이면 아래의 문장을 수행하지 않음
#     print(i) # 짝수는 찍혀나오지 않음 홀수만 찍혀나옴

# 반복문을 반대로 수행하기
# n = int(input("정수 입력 : "))
# for i in range(n, 0 - 1, -1): # 시작값, 최종값, 증감값
#     print(f"인덱스 : {i}")

# for문으로 알파벳 출력하기
# ASCII :
# chr() : 유니코드를 입력 받아 그 코드에 해당하는 문자를 출력
# ord() : 문자의 유니코드 값을 돌려주는 함수

# for i in range(ord("A"), ord("z")+1): # A = 65, a = 97
#     print(chr(i), end= " ")
# print()
#
# for i in range(65,91): #A:65 Z:90
#     print(chr(i), end= " ")
# print()



























































































