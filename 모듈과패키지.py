# # 모듈이란? 파이썬 코드를 포함하는 파일(.py)
# # 패키지? 여러 모듈을 포함하는 디렉토리
# # import math     # math 모듈을 import
# # print(math.sin(1))
# # print(math.cos(1))
#
# # from math import *
# # print(sin(1))
# # print(cos(1))
#
# # import math as m
# # print(m.sin(1))
# # print(m.cos(1))
#
# import sys
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# print("명절줄 인수 : ", sys.argv)
#
# print("실행 경로 : ", sys.path[0])
#
# import os
# cwd = os.getcwd()
# print(cwd)
#
# # # 디렉토리 생성
# # os.mkdir("testtest")
#
# # 파일 또는 디렉토리 존재 여부 확인
# is_file = os.path.isfile("password12.txt")
# print(is_file)
#
# is_dir = os.path.isdir("testtest")
# print(is_dir)
#
# os.system("dir")

# 모듈 만들기
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main()__":
    print(add(1,4))
    print(sub(4,2))













