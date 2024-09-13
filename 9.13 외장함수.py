# 외장함수는 import해서 사용하는 함수, 파이썬 기본적으로 제공하는 것
# 랜덤 함수 : 지정한 범위내에서 임의의 숫자를 만들어 내는 것
# import random
#
# # rand = random.randint(a:0, b:4)     # 0 ~ 4 까지의 임의의 값을 생성(미만 개념이 없음, 0도 포함 4도 포함)
#
# for i in range(30):
#     rand = random.randrange(1,11) # 1 ~ 10까지
#     print(rand, end="")
# print()

# 중복되지 않는 로또 번호 생선 : 1 ~ 45 사이의 임의의 수 6개
# 리스트를 사용하고, 리스트 내에 임의로 생성한 번호가 있으면, 추가하면 안됨
# if rand not in list:
# print("로또 번호 자동 생성 : ", end="")

# import random
# lotto = []
# while len(lotto) <= 6:
#    rand = random.randrange(1,46)
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6: break
# print(lotto)

