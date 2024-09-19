from datetime import datetime  # 날짜와 시간을 사용하기 위해서
import time  # 시간 관련 기능을 사용하기 위해 import

make_cnt = 0  # 전역변수, 생산 대수를 구하기 위해서

# 공통 선택 함수
def select_option(prompt, options):
    while True:
        print(prompt)
        for idx, option in enumerate(options, start=1):
            print(f"[{idx}] {option}")
        sel = input("선택하세요: ")
        if sel in map(str, range(1, len(options) + 1)):
            return sel

def choice_pad():
    return select_option("<< iPad Pro 구입하기 >>", ("구입하기", "종료하기"))

def select_screen():
    return select_option("디스플레이를 선택 하세요:", ("11인치", "13인치"))

def select_color():
    return select_option("컬러를 선택 하세요:", ("스페이스그레이", "실버"))

def select_memory():
    return select_option("용량을 선택 하세요:", ("128GB", "256GB", "512GB", "1TB"))

def select_network():
    return select_option("네트워크를 선택 하세요:", ("Wi-Fi", "Wi-Fi+Cellular"))

def select_name_service():
    sel = select_option("각인 서비스를 선택 하세요:", ("각인 서비스 신청", "신청 안함"))
    if sel == "1":
        return input("이름을 입력하세요: ")
    return "NONE"

def make_ipad(screen, color, memory, network, name):
    global make_cnt
    make_cnt += 1

    # 선택된 옵션에 따른 출력 (튜플 사용)
    screen_options = ("", "11인치", "12.9인치")
    color_options = ("", "스페이스그레이", "실버")
    memory_options = ("", "128GB", "256GB", "512GB", "1TB")
    network_options = ("", "Wi-Fi", "Wi-Fi+Cellular")

    # 시리얼 넘버 생성
    serial_screen = "11" if screen == "1" else "13"
    serial_network = "W" if network == "1" else "C"
    serial_date = datetime.today().strftime("%Y%m%d")
    serial_number = f"iPad{serial_screen}{serial_network}{serial_date}{make_cnt}"

    # iPad 제작 진행 표시 (30초 동안 진행률 표시)
    print("\n아이패드 제작중...")

    for i in range(1, 31):
        print(f"\r제작중... [{i * 100 // 30}%]", end='')  # 진행률 표시
        time.sleep(1)  # 1초 대기

    print("\n\niPad Pro가 출고 되었습니다.")
    print("=" * 34)
    print(f"화면 크기 : {screen_options[int(screen)]}")
    print(f"제품 색상 : {color_options[int(color)]}")
    print(f"제품 용량 : {memory_options[int(memory)]}")
    print(f"네트워크 : {network_options[int(network)]}")
    print(f"이름 : {name}")
    print(f"시리얼 넘버 : {serial_number}")
    print("-" * 34)

# 프로그램 실행
while True:
    if choice_pad() == "2":
        print("iPad Pro 구입을 종료합니다.")
        break

    screen = select_screen()
    color = select_color()
    memory = select_memory()
    network = select_network()
    name = select_name_service()
    make_ipad(screen, color, memory, network, name)
