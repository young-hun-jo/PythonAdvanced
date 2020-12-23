# Chapter04-03
# 파이썬 심화 - 시퀀스 형
# 해시테이블 : 적은 리소스로 많은 데이터를 효율적으로 관리 -> Python의 Dictionary를 이용하면 편리
# Dictionary -> key 중복 허용 X, Set(집합) -> 중복 허용 X

# Dict 구조
#print(__builtins__.__dict__) # Dict 자료구조 형태로 출력됨

# Hash 값(unique한 값) 뽑아내기 -> hash() 메소드 사용!
t1 = (10, 20, (30, 40, 50)) # tuple is immutable
t2 = (10, 20, [30, 40, 50]) # list is mutable
print('t1의 hash: ', hash(t1))
# print('t2의 hash: ', hash(t2)) -> list는 mutable해서 언제든 변경될 수 있기 때문에 해당 데이터가 고유의 값을 갖지 못하기 때문에 에러발생
print()

# Dict의 setdefault 예제 for tuple to dictionary
source = (('k1', 'value1'),
        ('k1', 'value2'),
        ('k2', 'value3'),
        ('k2', 'value4'),
        ('k2', 'value5'))
new_dict1 = {}
new_dict2 = {}

# setdefault를 사용하지 않고 일반적인 방법을 이용해 Dictionary로 전환!
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print("일반적인 방법 이용:", new_dict1)

# setdefault를 이용해 자동적으로 중복되는 key값 잘 처리해주기
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print("setdefault 방법 이용:", new_dict2)

# Dictionary comprehension을 이용하게 되면 중복되는 값들 중 마지막 값들만 처리됨
new_dict3 = {k: v for k, v in source}
print("Dict comprehension 이용:", new_dict3)
