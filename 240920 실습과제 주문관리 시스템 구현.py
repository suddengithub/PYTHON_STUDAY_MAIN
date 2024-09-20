from decimal import Decimal, ROUND_HALF_UP

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.products = []
        self.total = Decimal(0)

    def add_item(self, product: Product):
        self.products.append(product)
        self.total += product.get_price()

    def get_item(self, name):
        for product in self.products:
            if product.get_name() == name:
                return product
        return None

    def remove_item(self, name):
        product = self.get_item(names)
        if product :
            self.products.remove(product)
            self.total -= product.get_price()
            return True
        return False

    def calculate_final_price(self, tax_rate: Decimal) : # 판매세를 적용한 최종 가격을 계산하여 반환하는 메서드
        final_price = self.total * (1 + tax_rate)
        return final_price.quantize(Decimal("0.01"), rounding = ROUND_HALF_UP)

def main():
    order = Order()
    tax_rate = Decimal("0.01")

    while True:

        print(f"""[1]제품 추가 [2]제품 제거 [3]제품 목록보기 [4]제품 상세보기 [5]최종가격 계산(세금포함) [6]프로그램 종료""")

        sel = input("메뉴를 선택하세요 : ")

        if sel == "1":
            name = input("추가할 제품 입력 : ")
            price = input("제품 가격을 입력하세요 : ")
            product = Product(name, price)
            order.add_item(product)
            print(f"{name} 제품이 추가되었습니다.")
        elif sel == "2":
            name = input("제거할 제품 이름을 입력하세요: ")
            if order.remove_item(name):
                print(f"{name} 제품이 제거되었습니다.")
            else:
                print(f"{name} 제품을 찾을 수 없습니다.")
        elif sel == "3":
            if order.products:
                print("현재 주문된 제품 목록:")
                for product in order.products:
                    print(f"- {product.get_name()} : {product.get_price()}")
            else:
                print("현재 주문된 제품이 없습니다.")
        elif sel == "4":
            name = input("상세 정보를 볼 제품의 이름을 입력하세요 : ")
            product = order.get_item(name)
            if product :
                print(f"{product.get_name()} : {product.get_price()}")
            else :
                print(f"{name} 제품을 찾을 수 없습니다.")

        elif sel == "5":
            tax_rate = Decimal(input("세율을 입력하세요 (예: 0.1) : "))
            final_price = order.calculate_final_price(tax_rate)
            print(f"최종 가격 (세금 포함): {final_price}")
        elif sel == "6":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__" :
    main()