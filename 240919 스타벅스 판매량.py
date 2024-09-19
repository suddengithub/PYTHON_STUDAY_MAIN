file_name = "스타벅스 일일매출.txt"

with open(file_name, "r", encoding="utf-8") as file: # with는 반복문과 같이 보기
    header = file.readline() # readline이 한줄 읽는 것
    header_list = header.split()
    print(header_list)

    espresso = []
    americano = []
    latte = []
    cappuccino = []

    for line in file:
        data_list = line.split()
        espresso.append(int(data_list[1]))
        americano.append(int(data_list[2]))
        latte.append(int(data_list[3]))
        cappuccino.append(int(data_list[4]))

print(f"""{header_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso) / len(espresso)}""")
print(f"""{header_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano) / len(americano)}""")
print(f"""{header_list[3]} 전체 판매량 : {sum(latte)}, 일 평균 판매량 : {sum(latte) / len(latte)}""")
print(f"""{header_list[4]} 전체 판매량 : {sum(cappuccino)}, 일 평균 판매량 : {sum(cappuccino) / len(cappuccino)}""")

