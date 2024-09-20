# 연산자 오버로딩 : 연산자의 기본 기능을 사용자가 정의할 수 있게 한 것

# def over_sum(x, y):
#     return x + y
#
# print(over_sum(100, 200))
# print(over_sum(1.11, 2.22))
# print(over_sum("혜인", "하나")) # 정수를 더해주는 것을 문자열 더해주는게 신기한 일

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # '+' 연산자에 대응합니다. 객체끼리 덧셈 연산을 정의합니다.
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   #  '-' 연산자에 대응합니다. 객체끼리 뺄셈 연산을 정의합니다.
        return Vector2D(self.x - other.x, self.y - other.y)

v1 = Vector2D(1,2)
v2 = Vector2D(3,4)

v3 = v1 + v2
print(v3.x, v3.y)

v4 = 12 + 13
print(v4)