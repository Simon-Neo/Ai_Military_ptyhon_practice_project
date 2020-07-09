
from datetime import datetime
# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

peoples = ['홍길동', '성진', '심청이', '장발장', '심봉사']

print('step 1 ---------------------------------------')
for name in peoples:
    print(f"{name} 차례 입니다, 빵을 ", end='')
    if name == '장발장':
        print("드릴 수 없습니다.")
    else:
        print("하나 드리겠습니다.")


# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 없는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것

def is_ok_to_eat_bread(name, dont_eat_name):
    if name == dont_eat_name:
        return 0
    return 1

print('step 2 ---------------------------------------')
for name in peoples:
    print(f"{name}은 빵을 먹을 수 ", end='')
    if is_ok_to_eat_bread(name, '장발장') == 0:
        print(" 빵을 드릴 수 없습니다.")
    else:
        print(" 빵을 하나 드리겠습니다.")


# --------------------------------------------------------

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

print('step 3 ---------------------------------------')

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


def stamp(input_num):
    """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
    input_num = input_num + 1  # 오류가 발생하지 않는다 (global 안쓰면 오류 발생함)
    print(input_num)
    return input_num


num_stamp = stamp(num_stamp)  # 화면에 1이 출력된다
num_stamp = stamp(num_stamp)  # 화면에 2가 출력된다


# --------------------------------------------------------

# 4. 클래스 이용하기

print('step 4 ---------------------------------------')

# Parent class Trnasport -------------------------------------------------
class c_transport():
    # 요구사항
    # - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
    def __init__(self, name, price, start_time, arrive_time):
        self.name = name
        self.price = price
        self.start_time = start_time
        self.arrive_time = arrive_time

    def show_start_time(self):
        print('Start Time =\t', self.start_time)
    def show_arrive_time(self):
        print('Arrive Time =\t', self.arrive_time)
    def get_transprot_name(self):
        return self.name

    def show_all_infomation(self):
        self.show_start_time()
        self.show_arrive_time()

# class Airplane -------------------------------------------------
class c_airplane(c_transport):

    # - 비행기 클래스 만들기
    # 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
    # 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
    def __init__(self, name, price, start_time, arrive_time, is_ok_hydrate):
        c_transport.__init__(self, name, price, start_time, arrive_time)
        self.is_ok_hydrate = is_ok_hydrate

    def show_check_hydrate(self):
        if self.is_ok_hydrate == True:
            print("수하물을 맡겼습니다!")
        else:
            print("이 비행기는 수하물을 못맡깁니다!")

    def show_start_time(self):
        print(f"This Airplane |\t", end='')
        super().show_start_time()
    def show_arrive_time(self):
        print(f"This Airplane |\t", end='')
        super().show_arrive_time()

    def show_all_infomation(self):
        super().show_all_infomation()
        self.show_check_hydrate()

# class Train -------------------------------------------------
class c_train(c_transport):
    # - 기차 클래스 만들기
    # 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
    # 기능 : 출발시간, 도착시간 보기, 좌석등급 보기
    def __init__(self, name, price, start_time, arrive_time, class_of_seat):
        c_transport.__init__(self, name, price, start_time, arrive_time)
        self.class_of_seat = class_of_seat

    def show_your_class_seat(self):
        print(f'Your Class seat is {self.class_of_seat}.! ^^')

    def show_start_time(self):
        print(f"This Train |\t", end='')
        super().show_start_time()
    def show_arrive_time(self):
        print(f"This Train |\t", end='')
        super().show_arrive_time()

    def show_all_infomation(self):
        super().show_all_infomation()
        self.show_your_class_seat()

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것

start_time = datetime(2090, 11, 11, 11, 00, 00, 00)
arrive_time = datetime(1990, 11, 11, 11, 00, 00, 00)
print(arrive_time)
airplane_A0 = c_airplane('airplane_A0', 100, start_time, arrive_time, True)
print(f"{airplane_A0.get_transprot_name()}'s Infomation -----------------")
airplane_A0.show_all_infomation()
print()

start_time = datetime(1990, 11, 11, 11, 00, 00, 00)
arrive_time = datetime(2090, 11, 11, 11, 00, 00, 00)
airplane_A1 = c_airplane('airplane_A1', 7777777, start_time, arrive_time, True)
print(f"{airplane_A0.get_transprot_name()}'s Infomation -----------------")
airplane_A1.show_all_infomation()
print()

start_time = datetime(51, 11, 11, 11, 00, 00, 00)
arrive_time = datetime(3000, 11, 11, 11, 00, 00, 00)
train_A0 = c_train('train_A0', 300, start_time, arrive_time, 'A')
print(f"{train_A0.get_transprot_name()}'s Infomation -----------------")
train_A0.show_all_infomation()
print()

start_time = datetime.today()
arrive_time = datetime.today()
train_A1 = c_train('train_A1', 300, start_time, arrive_time, 'A')
print(f"{train_A1.get_transprot_name()}'s Infomation -----------------")
train_A1.show_all_infomation()
print()

