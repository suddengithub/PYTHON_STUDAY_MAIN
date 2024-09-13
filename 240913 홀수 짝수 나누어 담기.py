# 무작위 수를 공백으로 기준하여 입력 받아서, 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제
# print("입력 :", end=" ")
# number = list(map(int, input().split()))
# odd = list(filter(lambda x: x % 2 == 1, number)) # filter : 조건에 맞는것을 거르어 주는 기능
# even = list(filter(lambda x: x % 2 == 0, number)) # lambda : 1회성 함수 이용한다는 의미
#
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")

# number = list(map(int, input("입력 : ").split()))
# even = []
# odd = []
#
# for e in number:
#     if e % 2 == 0: even.append(e) # 2로 나눠서 나머지가 0이면 짝수
#     else: odd.append(e) # 그렇지 않으면 홀수
# print(f"홀수: {odd}")
# print(f"짝수: {even}")

number = list(map(int, input("입력 : ").split()))
even = []
odd = []

for e in number:
        if e % 2 == 0: even.append(e)
        else: odd.append(e)
print(f"홀수: {odd}")
print(f"짝수: {even}")






