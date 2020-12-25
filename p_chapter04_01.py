# Chapter 04-01
# 시퀀스형
'''
< 자료구조 구분 기준>
1-1. 컨테이너(Container) - 서로다른 자료형 구성 가능
    => list, tuple, collections.deque
1-2. Flat - 한 개의 자료형으로 구성
    => str, bytes, bytes array, array.array, memoryview

2-1. 가변 자료구조
    => list, bytes array, array.array, memoryview, deque
2-2. 불변 자료구조
    => tuple, str, bytes
'''
# ord(string)은 문자열의 유니코드 번호를 반환해줌
# 1.일반 list append
chars = '!@$##%$^%$^&'
code_lst1 = []
for c in chars:
    code_lst1.append(ord(c))
print("일반 list append: ", code_lst1)
# List comprehension => 데이터 양이 커지면서 이런 방법이 더 속도가 우세하다고 함!
code_lst2 = [ord(c) for c in chars]
print("list comprehension: ", code_lst2)
print('-'*50)
# ------------------------------------------------------------------
# Map, Filter는 iterator를 만듦!
# filter 함수는 filter(함수, iterable한 객체) => iterator가 결과기 때문에 next()를 이용해 출력 가능
filter_ = filter(lambda x: x > 40, [ord(c) for c in chars])
print("filter에 list감싸준 후 :", list(filter_))
# list로 감싸서 list형태로 만들어주자

# map 함수
map_ = map(ord, chars)
print([ord(c) for c in chars])
print('첫번째 요소:', next(map_))
print('두번째 요소:', next(map_))
print('세번째 요소:', next(map_))
# ------------------------------------------------------------------

# list comprehension VS Map + Filter
code_lst3 = [ord(c) for c in chars if ord(c) > 40]
code_lst4 = list(filter(lambda x: x > 40, map(ord, chars)))
print("list comprehension: ", code_lst3)
print("Map + Filiter: ", code_lst4)
print('-'*50)

# Generator 생성 -> 메모리를 절약하기 위해 데이터를 생성하기 직전 생성할 준비만 맞춰놓은 상태라고 할 수 있음!
# 한개의 자료구조를 갖으면서 가변적인 array 자료구조 사용해보기
import array

# Generator는 list comprehension 표현식에서 대괄호[] -> 소괄호()로 바꿔!
tuple_g = (ord(c) for c in chars)
print(tuple_g, type(tuple_g))
print([ord(c) for c in chars])  # list comprehension은 데이터를 모두 메모리에 올려버림..!
print(next(tuple_g))
print(next(tuple_g))

# Generaotr 이용해 4개의 반과 각 20개의 번호를 갖는 자료구조 생성
students_g = (f"{room}반 {num}번" for room in 'A B C D'.split() for num in range(1, 21))
print(students_g)
for student in students_g:
    print(student)

# Python의 얕은 복사 Vs 깊은 복사
marks1 = [['&'] * 3 for _ in range(4)]  # 얕은 복사
marks2 = [['&'] * 3] * 4    # 깊은 복사
print(marks1)
print(marks2)
print("일부 요소 수정 후")
marks1[0][0] = '#'
marks2[0][0] = '#'
print(marks1)
print(marks2)   # 한 위치의 데이터를 바꾸었는데 나머지도 다 바뀜 왜!? => list의 id가 동일여부 차이!
# list의 id 동일 여부 비교해보기
marks1_id = [id(l) for l in marks1]
marks2_id = [id(l) for l in marks2]
print(marks1_id)
print(marks2_id)
