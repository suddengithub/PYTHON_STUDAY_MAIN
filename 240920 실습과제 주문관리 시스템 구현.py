import decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = decimal.Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.products = []
        self.total = decimal.Decimal(0)

    def add_item(self, product):
        self.products.append(product)
        self.total += product.get_price()

    def get_item(self, name):
        for product in self.products:
            if product.get_name == name:
                return product
        return None

    def remove_item(self, name):
        product_to_remove = self.get_item(names)
        if product_to_remove:
            self.products.remove(product_to_remove)
            self.total -= product_to_remove.get_price()
            return True
        return False

    def calculate_final_price(self, tax_rate):
        return self.total * (1 + tax_rate).quantize(decimal.Decimal('0.01'))


while True:
    order = Order()
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
            print("\n현재 주문된 제품 목록:")
            for product in order.products:
                print(f"- {product.get_name()} : ${product.get_price()}")
        else:
            print("현재 주문된 제품이 없습니다.")
    elif sel == "4":
        if order.products:
            print("\n현재 주문된 제품 목록:")
            for product in order.products:
                print(f"- {product.get_name()} : ${product.get_price()}")
        else:
            print("현재 주문된 제품이 없습니다.")
    elif sel == "5":
        tax_rate = decimal(input("세율을 입력하세요 : "))
        final_price = my_order.calculate_final_price(Decimal(""))
        print(f"세금을 포함한 최종 가격: ${final_price}")
    elif sel == "6":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")
