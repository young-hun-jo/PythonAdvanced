# Chapter04-02
# 파이썬 심화 - 시퀀스 형
'''
< 자료구조 구분 기준>
1-1. 컨테이너(Container) - 서로다른 자료형 구성 가능
    => list, tuple, collections.deque
1-2. Flat - 한 개의 자료형으로 구성
    => str, bytes, bytes array, array.array, memoryview

2-1. 가변 자료구조
    => list, bytes array, array.array, memoryview, deque
2-2. 불변 자료구조
    => tupel, str, bytes
'''

# Tuple Advanced - unpacking
# b, a = a, b -> 이것도 일종의 unpacking임!
# *(aster)를 이용해 unpacking 가능
print(divmod(100, 21)) # 몫과 나머지 출력
print(divmod(*(100, 21))) # tuple (100, 21)을 unpack
print(*(divmod(100, 21))) # divmod결과값을 unpack
print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest= range(2) # 부족해도 빈 리스트로 반환
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
print()
print()

# Mutable(가변) VS Immutable(불변)
ex1 = (15, 20, 25) # tuple is immutable
ex2 = [15, 20, 25] # list is mutable
print(ex1, id(ex1))
print(ex2, id(ex2))
print()
# 하단의 방식은 tuple, list 둘다 새로운 메모리 주소(id)값이 부여됨
ex1 = ex1 * 2
ex2 = ex2 * 2
print(ex1, id(ex1))
print(ex2, id(ex2))
print()
# 하지만 하단의 방식으로 하면 tuple은 새로운 id값이 부여되지만 list는 연산 하기 전 id와 동일! 즉, 가변성임!
ex1 = (15, 20, 25) # tuple is immutable
ex2 = [15, 20, 25] # list is mutable
ex1 *= 2
ex2 *= 2
print(ex1, id(ex1))
print(ex2, id(ex2))
print()

## sorted VS sort : 공통인자로 reverse, key=len/str.lower/함수.. 가
# 1. sorted : 정렬 후 새로운 객체를 반환
v_list = ['bus', 'train', 'airplane', 'underground', 'car']
h_list = ['버스', '기차', '비행기', '지하철', '자동차']
print('sorted: ', sorted(v_list)) # 디폴트는 알파벳은 오름차순으로
print('sorted: ', sorted(h_list)) # 디폴트는 한글도 오름차순으로
print('sorted1: ', sorted(v_list, reverse=True))
print('sorted1: ', sorted(h_list, reverse=True))
print('sorted2: ', sorted(v_list, key=len))
print('sorted2: ', sorted(h_list, key=len))
print('sorted3: ', sorted(v_list, key=lambda x: x[-1],
                          reverse=True)) # 문자열 마지막 글자 기준으로 정렬
print('sorted3: ', sorted(h_list, key=lambda x: x[-1],
                          reverse=True))
print()

# 2. sort : 정렬한 후 기존 객체를 변경시킴(새로운 메모리 주소 부여하지 않고 기존 것 사용)
print('sort1: ', v_list.sort(), v_list) # sort() 기존의 것을 변경하기 때문에 None을 출력함
print('sort2: ', v_list.sort(reverse=True), v_list)
print('sort3: ', v_list.sort(key=len), v_list)
print('sort4: ', v_list.sort(key=lambda x: x[-1]), v_list)

## List vs Array 사용 케이스
# 1. 리스트 기반 : 유동적이고 다양한 자료형, 범용적 사용 시
# 2. 숫자 기반 : 머신러닝과 같이 수치형 연산을 사용하기 위해 즉, 데이터가 숫자로만 이루어졌을 시 사용




