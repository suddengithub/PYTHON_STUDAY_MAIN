# decimal 내장 모듈의 Decimal 클래스 및 반올림을 위한 round_half_up import
from decimal import Decimal, ROUND_HALF_UP


# Product 클래스 구현
class Product:
    def __init__(self, name: str, price: Decimal):  # name : 문자열 / price : decimal.Decimal
        self.name = name  # 인스턴스 변수 생성 및 초기화
        self.price = price

    def get_name(self):  # 제품의 이름을 반환하는 메서드
        return self.name

    def get_price(self):  # 제품의 가격을 반환하는 메서드
        return self.price


# Order 클래스 구현
class Order:
    def __init__(self):
        self.products = []  # 객체를 저장하는 리스트
        self.total = Decimal("0.00")  # 주문 내 모든 제품의 가격 합계를 Decimal 형식으로 저장하는 변수

    def add_item(self, product: Product):  # 제품 이름을 받아 Product 객체를 products 리스트에 추가하고 total을 업데이트하는 메서드
        self.products.append(product)  # Product 객체를 products 리스트에 추가하고
        self.total += product.get_price()  # total을 업데이트(추가)

    def get_item(self, name: str):  # 제품 이름을 받아 일치하는 Product 객체를 반환하는 메서드
        for product in self.products:  # products 리스트 내 product
            if product.get_name() == name:  # 입력한 이름과 일치하면
                return product  # Product 객체 반환
        return None  # 없으면 None 반환

    def remove_item(self, name: str):  # 제품 이름을 받아 일치하는 Product 객체를 products 리스트에서 제거하고 total을 업데이트하는 메서드
        product = self.get_item(name)
        if product:  # 입력받은 이름이
            self.products.remove(product)  # products 리스트에 있으면 제거하고
            self.total -= product.get_price()  # total을 업데이트(삭제)
            return True  # 성공 시 True 반환
        return False  # 실패 시 False 반환

    def calculate_final_price(self, tax_rate: Decimal):  # 판매세를 적용한 최종 가격을 계산하여 반환하는 메서드
        final_price = self.total * (1 + tax_rate)
        return final_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # 소수점 3번째 자리에서 반올림


def main():  # 메뉴를 보여주는 메서드
    order = Order()
    tax_rate = Decimal("0.01")  # 세금 10%

    while True:
        print("[1] 제품 추가")
        print("[2] 제품 제거")
        print("[3] 제품 목록 보기")
        print("[4] 제품 상세 보기")
        print("[5] 최종 가격 계산 (세금 포함)")
        print("[6] 프로그램 종료")

        sel = input("메뉴를 선택하세요 : ")

        if sel == "1":
            name = input("제품 이름을 입력하세요: ")
            price = Decimal(input("제품 가격을 입력하세요: "))
            product = Product(name, price)
            order.add_item(product)
            print(f"{name} 제품이 추가되었습니다.")

        elif sel == "2":
            name = input("제거할 제품의 이름을 입력하세요: ")
            if order.remove_item(name):
                print(f"{name} 제품이 제거되었습니다.")
            else:
                print(f"{name} 제품을 찾을 수 없습니다.")

        elif sel == "3":
            if order.products:
                print("제품 목록:")
                for product in order.products:
                    print(f"- {product.get_name()} : {product.get_price()}")
            else:
                print("등록된 제품이 없습니다.")

        elif sel == "4":
            name = input("상세 정보를 볼 제품의 이름을 입력하세요 : ")
            product = order.get_item(name)
            if product:
                print(f"{product.get_name()} : {product.get_price()}")
            else:
                print(f"{name} 제품을 찾을 수 없습니다.")

        elif sel == "5":
            tax_rate = Decimal(input("세율을 입력하세요 (예: 0.1) : "))
            final_price = order.calculate_final_price(tax_rate)
            print(f"최종 가격 (세금 포함): {final_price}")

        elif sel == "6":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 요청입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()