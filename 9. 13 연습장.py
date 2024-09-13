# print(100, 200, sep="\n")
# print("010", "1234", "5678", sep="-")
#
# 파이썬 스타일 2, 가장 최근에 추가된 방식(f-string), 3.6 이후
# f와 {}로 사용 합니다.
name = "정경수"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "경기도 수원시"

print("====== 파이썬 스타일 2 ======")
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {jobs}")
print(f"주소 : {addr}\n")