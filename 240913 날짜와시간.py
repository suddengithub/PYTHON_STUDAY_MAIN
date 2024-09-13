# 날짜와 시간 관련 함수
from datetime import datetime   # datetime 모듈에서 datetime함수를 가져옴


print(datetime.today())
print(datetime.today().month)
print(datetime.today().date())
print(datetime.today().time())
print(datetime.today().hour)
print(datetime.today().day)
print(datetime.today().weekday()) # 0: 월요일 1:화요일
print()
import calendar
# print(calendar.calendar(2024))

# math 모듈 : 수학과 관련된 기능을 처리할 떄 사용
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.00000000001)) # 소수점 이하가 있으면 무조건 올림 ceiling 천장
print(math.floor(1.99999999999)) # 소수점 이하는 무조건 날림 floor 바닥




