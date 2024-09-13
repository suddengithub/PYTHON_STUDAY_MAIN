# 입력 : 5
# 2중 for문을 사용해서 풀어야 합니다.
# *
# **
# ***
# ****
# *****

# n = int(input("별 입력: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

n = int(input("입력 : "))
for i in range(n): # 행의 개수
    for j in range(i+1):
        print("*", end="")
    print()

# n=1을 넣으면 1미만이므로 i는 0값(첫번쨰) j도 0값(1개) 그래서 별이 한개에 찍혀나옴
# n-2을 넣으면 2미만이므로 i는 0값(첫번쨰), 1값(두번쨰), j도 0값(1개) 1값(2개) 그래서 별이 2개까지 찍혀나옴

# n = int(input("입력 : "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
#
