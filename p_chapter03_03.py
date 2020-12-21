# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method) = 이미 built-in 되어 있는 메소드들 의미!
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

### 네임드 튜플! ### => 튜플 성질을 지니지만 dictionary처럼 key, value 형태를 가질 수 있음!
from collections import namedtuple
from math import sqrt

# 네임드 튜플 정의하는 방법(총 4가지)
Point1 = namedtuple('Point1', 'x y')
Point2 = namedtuple('Point2', 'x, y')
Point3 = namedtuple('Point3', ['x', 'y'])
Point4 = namedtuple('Point4', 'x, y, x, class',
                    rename=True) # 중복된 key 이름 또는 class같은 예약어 이름과 동일할 때 key값으로 지정해주기 위한 파라미터

pt1 = Point1(30, 10)
pt1_2 = Point1(x=30, y=10) # 지정한 key값 이용도 가능
print(pt1)
print(pt1_2)
print('-'*50)
# namedtuple을 이용해서 두 점 간의 유클리디안 거리 구하기
pt1 = Point1(5, 6)
pt2 = Point1(3, 9)
dist = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2) # 물론 key인 x,y대신 [0],[1] 처럼 인덱스도 사용가능하지만 가독성이 key값을 이용하는 것이 더 좋음!
print(dist)
print('-'*50)
#-------------------------------------------------------------------------------------------------
# Dictionary to Namedtuple
temp_dict = {'x': 75, 'y': 55} # key이름은 namedTuple의 key 이름과 동일하도록 설정
temp_Point = Point1(**temp_dict)
print(temp_Point)
print('-'*50)
 ## 참고로 container들은 * 또는 **를 붙여서 unpacking 가능
a = [1,2,3]
b = (4,5,6)
c = {'A':1, 'B':2, 'C':3}
print(*a)
print(*b)
print(*c)
  ## dictionary는 **를 붙이면 특정 key의 value들과 같이 unpacking됨 ->함수인자 넣을 와 네임드 튜플 정의에 활용됨때
def sum(A, B, C):
    print(A + B + C)
sum(**c)
print('-'*50)
#-------------------------------------------------------------------------------------------------

# 네임드 튜플 메소드
# 1. _make() : 새로운 객체를 생성 - list to namedtuple
temp = [52, 39]
pt4 = Point1._make(temp)
print(pt4)
# 2. _fields : 필드 네임(namedtuple의 key값들) 확인
print(pt4._fields)
# 3. _asdict() : namedtupe -> OrederedDict로 변환
print(pt4._asdict()) #디폴트는 key 기준으로 정렬되는 듯함!
print('-'*50)

#### 네임드 튜플 실습 ####
# 4개의 반(A,B,C,D)가 있고 각 20명의 학생이 있을 때, 각 학생별 반-번호 네임드 튜플 만들기
# namedtuple 정의
Classes = namedtuple('Classes', 'room, number')
rooms = 'A B C D'.split()
numbers = [str(n) for n in range(1, 21)]

# 이중 for 문 list comprehension 이용
students = [Classes(room=room, number=number) for room in rooms for number in numbers]
print(len(students))

# 코드 가독성 위한 리팩토링
students = [Classes(room, number)
            for room in 'A B C D'.split()
                for number in [str(n) for n in range(1, 21)]]
print(len(students))

# 각 학생들의 반-번호 출력
for idx, s in enumerate(students):
    print(f"{idx+1}번 학생은 {s.room}반, {s.number}번 학생입니다.")


