# Chapter06-02
# 병행성(Concurrency)
# iterator, generator

# 파이썬 반복가능한 자료구조
# collections의 자료구조, text file, list, dict, set, tuple, unpacking, *args, **kwargs

# 1.yield 실습해보기
# Generator Ex1)
def generator_1():
    print('Started!')
    yield 'Number1'
    print('Keep going!')
    yield 'Number2'
    print("Ended!")
print(generator_1()) # 함수 자체가 generator object로 출력됨!

temp = iter(generator_1())
print(temp) # 이미 generator이기 떄문에 iter메소드를 씌워도 이미 generator object로 출력됨! ->저번 예시에서는 class였기 때문에 클래스의 iter 매직메소드를 이용하기 위해 iter()해준것임!
# <결과는 동일>
# print(next(temp))
# print(next(generator_1()))
print('-'*50)

for v in generator_1():
    print(v)
print('-'*50)

# Generator Ex2
temp2 = [x * 3 for x in generator_1()] # list comprehension
temp3 = (x * 3 for x in generator_1()) # generator
print(temp2)
print(temp3) # generator 객체!
print('-'*50)

print('<temp2 : list comprehension>') # yield에 할당된 값들만 반환
for t2 in temp2:
    print(t2)
print('<temp3 : generator>') # generator_1()이라는 함수이자 generator안에서 정의된 print문까지 출력(단, *3연산은 yield에 할당된 값들만 적용된 것은 list comprehension과 동일)
for t3 in temp3:
    print(t3)
print('-'*50)

# Generaotr Ex3) -> itertools의 여러가지 메소드
# count, takewhile, filterfalse, accumulate, chain, product, groupby
import itertools
# 1.count : 무한으로 생성
gen1 = itertools.count(1, 2.5) # 1부터 2.5씩 커지는데 무한대까지...
print(gen1, type(gen1)) # itertools.count 라는 일종의 클래스!
# next 매직 메서드를 사용해 generator 하나씩 호출해서 값 1개씩 반환
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print('-'*50)
# 2. takewhile : 특정 조건에 해당하는 값들만 모아 generator 생성
gen2 = itertools.takewhile(lambda n : n < 500, itertools.count(2, 5))
# for문으로 generator 출력
for v in gen2:
    # print(v)
    pass
print('-'*50)

# 3. filterfalse : 특정 필터(조건)에 해당하지 않는! 요소들을 모아 generator 생성
gen3 = itertools.filterfalse(lambda n : n < 2, [x for x in range(10)])
print(list(gen3))

# 4. accumulate : 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 10)])
print(list(gen4))

# 5. chain : 두 자료구조를 연결 -> 연결 후 리스트 자료구조로 반환!
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
gen5_1 = itertools.chain(('A','B','C'), range(1, 11, 2))
gen5_2 = itertools.chain(('A','B','C'), [1,2,3,4,5]) # tuple & list
gen5_3 = itertools.chain(enumerate('ABCDE')) # index, value 튜플로 묶어 반환
print(list(gen5))
print(list(gen5_1))
print(list(gen5_2))
print(list(gen5_3))
print('-'*50)

# 6. product : 경우의 수 구하기(repeat >=2) 즉, r개의 데이터를 뽑아 일렬로 나열하는 경우(순열) 그리고 원소를 중복해 뽑음!
# default -> repeat=1이기 떄문에 'ABC'의 각 개별 요소를 할당
gen6 = itertools.product('ABC')
lst = list(gen6)
print(lst)
print(lst[0], type(lst[0]), 'index는 0까지밖에 없음: ', lst[0][0])
# print(lst[0][1]) # 에러발생
gen6_2 = itertools.product('ABC', repeat=2)
print('## product example')
print(list(gen6_2))

# 6-1. permutation : r개의 데이터를 뽑아 일렬로 나열(순열) 단, 원소를 중복해 뽑지 않음!
gen6_3 = itertools.permutations('ABC', r=2)
print('## permuation example')
print(list(gen6_3))

# 6-2. combinations : r개의 데이터를 뽑아 순서를 고려하지 않고 나열(조합). 단, 중복해 뽑지 않음!
gen6_4 = itertools.combinations('ABC', r=2)
print('## combinations example(중복X)')
print(list(gen6_4))

# 6-3. combinations_with_replacement : r개의 데이터를 뽑아 순서롤 고려하지 않고 나열(조합). 단, 중복해 뽑음!
gen6_5 = itertools.combinations_with_replacement('ABC', r=2)
print('## combinations_with_replacement example')
print(list(gen6_5))
print('-'*50)
# 7. groupby : 똑같은 값들끼리 그룹핑
gen7 = itertools.groupby('AAABBBCDDEEFFFFF')
# print(list(gen7)) # 튜플의 두번째 요소가 grouper 이라는 객체
for k, v in gen7:
    print(k, '>', list(v))



