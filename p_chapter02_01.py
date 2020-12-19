# 객체 지향 프로그래밍(OOP) => 코드의 재사용, 코드 중복 방지 등 위함!

## 1.일반적인 코딩 ## => 너무 반복되는 코드 발생.. 데이터 변경 시 관리도 어려
car_company_1 = 'Hyundai'
car_detail_1 = [
    {'color':'white',
     'horsepower': 400,
     'price': 8000}
]
car_company_2 = 'Samsung'
car_detail_2 = [
    {'color':'black',
     'horsepower': 500,
     'price': 5000}
]
car_company_3 = 'Audi'
car_detail_3 = [
    {'color':'blue',
     'horsepower': 900,
     'price': 10000}
]

## 2.리스트 구조 ## => 리스트 내에서 특정 데이터 삭제하려면 인덱스로 접근해야 함
# -> 데이터 개수가 많아지면 인덱스 작성시 실수 유발 가능성 농후
car_company_lst = ['Hyundai', 'Samsung', 'Audi']
car_detail_lst = [
    {'color': 'white', 'horsepower': 400, 'price': 8000},
    {'color':'black','horsepower': 500,'price': 5000},
    {'color':'blue','horsepower': 900, 'price': 10000}
]

# 특정 데이터 삭제하기 위해 del 또는 pop 사용
del car_company_lst[0]
car_detail_lst[0].pop('color')
print(car_company_lst)
print(car_detail_lst)
print('-'*50)

## 3.딕셔너리 구조 ## => 코드 반복 지속, 중첩 문제, 키 조회시 예외 처리 등 문제 발생
cars_dicts = [
    {'car_company': 'Hyundai',
     'car_details': {'color': 'white', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Samsung',
     'car_details': {'color':'black','horsepower': 500,'price': 5000}},
    {'car_company': 'Audi',
     'car_details': {'color':'blue','horsepower': 900, 'price': 10000}}
]

# 딕셔너리 내에서 특정 데이터 삭제
del cars_dicts[1]
print(cars_dicts)
print('-'*50)

## 4.클래스 구조 ## => 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
# Car(object) == Car 둘 다 아무거나 정의해도 상관 없음 -> style 문제
class Car(object):
    def __init__(self, company, detail):
        self._company = company
        self._detail = detail
    # Python에 내장되어 있는 메소드를 활용해서 인스턴스에 있는 정보 출력 가능
    # __str__은 사용자 입장에서 사용하는 출력 메서드
    def __str__(self):
        return f"{self._company}: {self._detail}"
    # __repr__ (representation)은 개발자 입장에서 사용하는 출력 메서드
    def __repr__(self):
        return f"{self._company}: {self._detail}"

car1 = Car('Hyundai', {'color': 'white', 'horsepower': 400, 'price': 8000})
print(car1)
# __dict__를 통해 현재 정의되어있는 네임 스페이스 정보 알아낼 수 있음!
print(car1.__dict__)
print('-'*50)

car2 = Car('Samsung', {'color':'black','horsepower': 500,'price': 5000})
car3 = Car('Audi', {'color':'blue','horsepower': 900, 'price': 10000})

cars = [car1, car2, car3]
car_lst = [x for x in cars]
print(car_lst)
print('-'*50)
# __repr__이든 __str__이든 일종의 함수이기 때문에 bracket을 사용해서 메서드 호출 가능
print(repr(car1))
print(str(car1))

