color = ("black", "brown", "red", "orange", "yellow", \
         "green", "blue", "violet", "grey", "white")
f_name = color.index(input("첫번쨰 값 : "))     # 해당 문자열의 인덱스 반환
s_name = color.index(input("두번쨰 값 : "))
t_name = color.index(input("세번쨰 값 : "))
print(f"저항값 : {int(str(f_name) + str(s_name)) * (10 ** t_name)}")  # 10의 승수 x 세번째 색상의 저항값
