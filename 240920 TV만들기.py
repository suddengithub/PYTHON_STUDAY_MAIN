# 클래스란? 객체(붕어빵)를 만들기 위한 설계도면(붕어빵 틀), 상태값을 저장하는 변수, 동작을 규정하는 메서드가 포함
# 키워드는 class
# 객체란? 클래스를 실체화 한 것
# 상속 : 부모 클래스의 특성을 자식 클래스에 물려주는 것
# 캡슐화 : 내부의 멤버(변수)를 외부에서 접근할 수 없도록 하는 것, 접근을 위한 게터(값을 읽는 메서드)와 세터(값을 쓰는 메서드) 메서드 필요
# 다형성 : 부모의 특성을 물려받아 특성을 변경하거나 개선하는 행위(오버로딩(파이썬 - X), 오버라이딩(파이썬 - O)
# 추상화 : 객체화가 되지 않는 부모로부터 특성을 물려 받는 것(추상클래스)
# 클래스의 이름 파스칼표기법(첫자가 대문자)
# 클래스를 만들기 위해서는 생성자가 필요(__init__())
# 생성자는 클래스가 객체로 만들어질 때 불려짐(내부의 인스턴스 변수를 초기화하는 목적으로 사용)
class Television:
    def __init__(self, name, is_on, channel, volume):
        self.name = name    # 인스턴스 변수를 생성하고 생성자의 매개변수 변수를 통해서 초기값을 입력 받음
        self.is_on = is_on  # TV의 전원 ON/OFF
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        self.channel = cnl
    def set_volume(self, vol):
        if 0 <= vol <= 100:
            self.volume =vol
        else:
            print("볼륨값 허용 범위를 벗어났습니다.")

    def set_info(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume()}")

lg_tv1 = Television("우리집TV", False, 11, 10)
lg_tv2 = Television("우리집TV", False, 11, 10)

lg_tv1.set_on(True)
lg_tv1.set_volume(1000)
lg_tv1.set_channel(59)
lg_tv1.tv_info()







