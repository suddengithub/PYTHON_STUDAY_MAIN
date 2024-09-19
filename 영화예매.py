seat = [0] * 10  # 0으로 초기화된 리스트 10개 생성
PRICE = 12000

def print_seat():
    for e in seat:
        if e == 0:
            print("[ ]", end=" ")
        else:
            print("[V]", end=" ")
    print()

def select_seat():
    print_seat()
    seat_num = int(input("좌석번호 입력 : ")) - 1  # 0번 인덱스 부터 시작하기 때문에
    if seat[seat_num] == 0: # 아직 예약 안된 좌석
        seat[seat_num] = 1
        print_seat()  # 예약 성공 시 결과 보여주기
    else:
        print("이미 예약된 좌석 입니다.")

def total_account():
    cnt = 0   # 판매된 좌석 개수를 누적
    for e in seat:
        if e == 1:
            cnt += 1
    return PRICE * cnt   # 티켓 가격 * 판매 좌석 수

while True:
    print("[1]예매하기")
    print("[2]종료하기")
    sel = int(input("메뉴 선택 : "))
    if sel == 1:
        select_seat()
    else:
        print(f"총 매출액 : {total_account()}")
        break