# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 클래스 정의
class Car():
    # 클래스 변수 정의
    price_per_raise = 1.0

    def __init__(self, company, detail):
        self._company = company
        self._detail = detail

    def __str__(self):
        return f"{self._company} - {self._detail}"

    # 인스턴스 메소드 - 가격 상향 전
    def detail_info(self):
        #print(id(self))
        print(f"Company:{self._company} - Price:{self._detail.get('price')}")
        return
    # 인스턴스 메소드 - 가격 상향 후
    def detail_info_after(self):
        print(f"Company:{self._company} - Price:{self._detail.get('price') * Car.price_per_raise}")
        return

    # 클래스 메소드 : 클래스 변수를 조작하고 이용하기 위한 메소드
    # cls = Car 클래스를 나타낸다고 생각하면 됨!
    @classmethod
    def raise_price(cls, per):
        if per <= 1.0:
            print("Please enter 1 or more.")
            return
        cls.price_per_raise = per
        return "Success! Price is increased!"

    # Static 메소드 : 클래스 변수를 이용하진 않지만 유동적으로 사용하고 싶을 때! Static 메소드는 cls, self같은 파라미터 받지 않음!
    # ex. 어떤 차가 현대 차인지 알아보기 위한 메소드 정의!
    @staticmethod
    def is_hyundai(instance):
        if instance._company == 'Hyundai':
            return "This car is a kind of Hyundai cars."
        return "This is not a kind of Hyundai cars."

car1 = Car('Hyundai', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('Samsung', {'color':'black','horsepower': 500,'price': 5000})

print("Before")
car1.detail_info()
car2.detail_info()
# 가격 상승시키는 클래스 메소드 호출!
Car.raise_price(1.5)
print("After")
car1.detail_info_after()
car2.detail_info_after()
print('-'*50)

# Static 메소드 호출 2가지 방법
# 1. 인스턴스로 호출하기
print(car1.is_hyundai(car1))
print(car2.is_hyundai(car2))
# 2. 클래스로 호출하기
print(Car.is_hyundai(car1))
print(Car.is_hyundai(car2))




