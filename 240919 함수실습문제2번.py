# 두번째 수 찾기
# 입력 : 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾을 수 : 3
# 해당 수의 위치를 반환 : 인덱스가 아님(=> 0이 아닌 실제 해당하는 위치를 찾아라), 9번째 <-> 인덱스를 찾아라(=> 0부터 계산해서 위치를 찾아라)
# 찾지 못하면 -1을 반환
def second_find(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i + 1
            else: cnt += 1
    return -1

# 정수값에 대한 리스트 입력 생성
ls = list(map(int, input("정수값 리스트 입력 : ").split()))
# 찾을 수 입력 받기
find_num = int(input("찾을 수 입력 : "))
# 결과 출력하기
print(second_find(ls, n))
