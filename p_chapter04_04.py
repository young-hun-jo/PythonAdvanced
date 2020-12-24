# Chpater04-04
# 파이썬 심화 - 시퀀스형
# 해시테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 X, Set -> 중복 값 허용 X
# Dict 및 Set 심화

# 원래 Dict는 mutable 하지만 Immutable한 Dict로 만들 수 있음!
# 라이브러리 이용
from types import MappingProxyType

d = {'key1': 'value1'}
d_frozen = MappingProxyType(d)
print("d와 d_frozen의 형태는 동일한가?", d == d_frozen)
print("d와 d_frozen의 메모리 주는 동일한가?", d is d_frozen)
print()

# 일반 dict 수정하기
d['key2'] = 'value2'
print("수정 후 d :", d)

# Immutable dict 수정해보기
# d_frozen['key1'] = 'value2' => error 발생
print()

# Set 선언하기
s1 = {'apple', 'banana', 'kiwi', 'apple', 'banana'}
s2 = set(['apple', 'banana', 'kiwi', 'apple', 'banana'])
s3 = {'orange'}
s4 = set() # {}로 선언하면 set이 아닌 empty dict로 정의됨!
# set에 데이터 첨가
s1.add('orange')
s2.add('watermelon')
s2.update(['pear', 'grapes']) # 여러개 첨가할땐 update!
s2.remove('kiwi') # 삭제할땐 삭제할 데이터 인자로 넣기
print(s1)
print(s2)
print(s3)
print(s4)

# Comprehension set => list comprehension과 비슷
result = {i for i in range(10)}
print(result, type(result))
print()
# 자료구조 선언시 최적화 하기
# 어떤 방법이 최적화 방법인지 알기 위한 dis 라이브러리 정의
from dis import dis
# dis 메소드안에 문자열 처럼 따옴표 안에 코드를 넣어주기!
print('-'*40)
print("선언 방법: 1", dis('{10}'))
print('-'*40)
print("선언 방법: 2", dis('set([10])'))

