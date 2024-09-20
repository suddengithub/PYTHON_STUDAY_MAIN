# 커피 메뉴 만들기
# [1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 불러오기 [6] 저장하기 [7] 분류별 보기 [8] 종료하기
# 기본 메뉴 만들기
# 카테고리별 조회 추가하기
import json

menu = {
    "Americano": ["Coffee", 2000, "기본 커피입니다."],
    "Espresso" : ["Coffee", 2500, "진한 커피입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]\
}
file_name = "menu.json"
# 파일에서 메뉴를 읽어오는 함수
def load_menu():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 없습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일에 저장하는 함수
def save_menu():
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)

# [1] 메뉴 보기
def print_menu():
    # for key in menu:
    #     print(f"{key} : {menu[key]}")
    for key, value in menu.items():
        print(f"{key} : {value}")

# [2] 메뉴 조회(개별 메뉴)
def get_menu(key):
    if key in menu:
        print(menu[key])
    else:
        print("찾는 메뉴가 없습니다.")

# [3] 메뉴 추가
def add_menu(key, category, price, desc):   # key, 분류, 가격, 설명
    if key not in menu: # 해당 키에 대한 메뉴가 없음
        menu[key] = [category, price, desc]
        print(f"{key} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재합니다.")
# [4] 메뉴 삭제
def del_menu(key):
    if key in menu:
        del menu[key]
        print(f"{key} 메뉴가 삭제 되었습니다.")
    else:
        print("삭제할 메뉴가 없습니다")
# 카테고리별 보기
def get_category(cate):
    for key, value in menu.items(): # items는 key값과 value값을 한꺼번에 뽑아낸다.
        if cate == value[0]:
            print(key, value[0], value[1], value[2])

def main():
    order = Order()

while True:
    print("메뉴를 선택하세요 : ")
    sel = input("[1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 불러오기 [6] 저장하기 [7] 분류별 보기 [8] 종료하기 : ")
    if sel == "1":
        print_menu()
    elif sel == "2":
        key = input("조회할 메뉴 입력 : ")
        get_menu(key)
    elif sel == "3":
        key = input("추가할 메뉴 이름 : ")
        cate = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("제품 설명 : ")
        add_menu(key, cate, price, desc)
    elif sel == "4":
        key = input("삭제할 메뉴 입력 : ")
        del_menu(key)
    elif sel == "5":
        menu = load_menu()
    elif sel == "6":
        save_menu()
    elif sel == "7":
        name = input("카테고리 입력 : ")
        get_category(name)
    elif sel == "8":
        print("영업을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")






























