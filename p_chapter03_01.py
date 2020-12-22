# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method) = 이미 built-in 되어 있는 메소드들 의미!
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# int도 하나의 Class로 정의되어 있다!
print(int)
print('-'*50)
# dir 메소드를 통해 매직 메소드 확인해보기
print(dir(int))

n = 10
# + 와 같은 연산자는 근본적으로 __add__라는 매직메소드로 구현되어 있는 것임!
print(n + 100)
print(n.__add__(100))
print(n * 30)
print(n.__mul__(30))

# 과일 클래스를 사용해서 메직 매소드 customizing 하기!
class Fruit:
    # 클래스 변수 정의
    discount_rate = 1.0

    def __init__(self, name, price):
        self._name = name
        self._price = price

    # str 매직 메소드 정의(클래스 할당하고 run하면 출력되는 정보)
    def __str__(self):
        return "{} - {}".format(self._name, self._price)

    # add 매직 메소드를 내 맘대로 정의해보기
    def __add__(self, other_inst):
        return (self._price + other_inst._price)

    # mul 매직 메소드를 내 맘대로 정의해보기
    def __mul__(self, other_inst):
        return (self._price * other_inst._price)

    # le(less) & ge(greater) 대소비교 매직 메소드 내맘대로 정의해보기
    def __le__(self, other_inst):
        if self._price <= other_inst._price:
            return True
        return False

    def __ge__(self, other_inst):
        if self._price >= other_inst._price:
            return True
        return False
    # 할인 된 가격 제공하는 인스턴스 메소드
    def calc_discount(self):
        return "Discounted price: {}".format(self._price * Fruit.discount_rate)
    # 할인률 커스터마이징 위한 클래스 메소드 정의
    @classmethod
    def change_rate(cls, rate):
        if rate >= 1.0:
            print("No longer applied to discount")
        cls.discount_rate = rate

    # 할인율 상승하
f1 = Fruit('orange', 2000)
f2 = Fruit('melon', 5500)

add = f1 + f2
print("Example")
print(add)
print('-'*50)
mul = f1 * f2
print(mul)
print('-'*50)
print(f1 <= f2)
print('-'*50)
print(Fruit.calc_discount(f1))
print('-'*50)
# 할인율 변경!
Fruit.change_rate(0.5)
print(Fruit.calc_discount(f1))