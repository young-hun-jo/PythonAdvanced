# 객체 지향 프로그래밍(OOP) => 코드의 재사용, 코드 중복 방지 등 위함!

class Car(object):
    # Docstring => Class.__doc__으로 클래스에 대한 설명 정보 출력 가능!
    """
    Car Class : 자동차 클래스
    Author : Jo
    Datetime : 2020-12-19
    """
    # 클래스 변수 정의
    car_count = 0

    def __init__(self, company, detail):
        self._company = company
        self._detail = detail
        # self.car_count = 100
        # 클래스 변수 이용하기
        Car.car_count += 1

    def __str__(self):
        return "{} - {}".format(self._company, self._detail)

    def __repr__(self):
        return '{} - {}'.format(self._company, self._detail)

    # del 메소드 생성해서 클래스 변수 감소시켜보기
    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print("Current ID :", id(self))
        print("Detail info: ", self._detail.get('price'))

# 이것이 Self : '자기 자신'!
car1 = Car('Hyundai', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('Samsung', {'color':'black','horsepower': 500,'price': 5000})
car3 = Car('Audi', {'color':'blue','horsepower': 900, 'price': 10000})

# self의 고유 id 확인하는 메서드
print(id(car1))
print(id(car2))
print(id(car3))
print('-'*50)

# 클래스 자체 id는 동일함!
print(id(car1.__class__) == id(car2.__class__))

# self의 attribute 확인하기
print(car1._company == car2._company)
print(car1 is car2) # id가 다르기 때문에 False!
print('-'*50)

# Docstring 출력
print(Car.__doc__)

# 만든 인스턴스 메소드 실행
car1.detail_info()
Car.detail_info(car1) # PEP 문법적으로 더 권장됨!
print('-'*50)

# dir & dict 차이 보기
print(dir(car1)) # (좀 포괄적인데) 사용가능한 모든 메소드 리스트
print(car1.__dict__) # 인스턴스 변수에 담긴 정보 출력!
print('-'*50)
# 클래스 변수(모든 인스턴스가 공유 가능함!)
# dir & dict로 클래스 변수는 어디에 있는지 확인 => self 인스턴스의 dir에 나타남!
print(dir(car1))
print(car1.__dict__) # car1.__dict__에는 공유하고 있는 클래스 변수 안나타남!
print('-'*50)

# 클래스 변수를 클래스 뿐만아니라 모든 인스턴스가 공유하는지 확인
print(Car.__dict__)
print(dir(car1))
print(dir(car2))
print(dir(car3))
print('-'*50)

# 만약 클래스 변수와 인스턴스 변수가 동일한 이름이라면
# 우선, 인스턴스 변수에서 찾고 -> 없을 시, (상위인) 클래스 변수로 찾아감!
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print('-'*50)

# 생성한 del 메소드 이용해서 클래스 변수(car_count) 감소시켜보기
del car2
del car3
# del한 후 클래스 변수 정의할 때는 삭제하지 않고 남아있는 self 인스턴스 이용해 호출하거나
# 클래스를 이용해 클래스 변수 호출
print(car1.car_count)
print(Car.car_count)

