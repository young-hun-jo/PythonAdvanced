# Chapter05-01
# 일급 함수(일급 객체) 의 특징들
# 1.런타임 초기화 => 실행 시점에 초기화
# 2.변수 할당 가능 => 함수를 변수에 할당 가
# 3.함수 인수 전달 가능 => 함수를 함수 인자에 전달
# 4.함수 결과 반환 가능 => 함수 결과를 다른 함수 결과값에 할당

# 일반 함수 만들어보기
def factorial(n):
    """factorial function -> n : int """
    # 재귀함수 종단 조건
    if n < 2:
        return 1
    else:
        return n + factorial(n-1)

# 일반 Class 만들기
class A:
    pass

print(factorial.__doc__)
print(factorial(4))
print(type(factorial), type(A)) # 함수도 일종의 클래스
# function 클래스만 갖고 있는 매직 메서드 살펴보기
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)
print('-'*50)
print()

# 2. 일급객체 특징 : 함수를 변수로 할당 가능
var_func = factorial
print(type(var_func))
print(var_func(5))
# map 함수 이용해보기
print(list(map(var_func, range(1, 12))))
print('-'*50)

# 3. 일급객체 특징 : 함수를 함수 인자에 전달 => 고위(high-order) 함수
# filter에서 익명함수를 정의해 리스트를 필터링한 후 이를 var_func 함수에 map을 이용해 적용!
print(list(map(var_func, filter(lambda x: x % 2, range(1, 11)))))
print([var_func(i) for i in range(1, 11) if i % 2])
print('-'*50)
# reduce() 메소드 사용방법 -> reduce(함수, 리스트객체)
from functools import reduce
from operator import add

print(reduce(add, range(1, 5)))
print(sum(range(1, 5)))

# 익명함수 : lambda -> 가급적 주석을 사용하되 되도록이면 일반함수 형태로 작성하는게 권장(가독성 위해)
print(reduce(lambda x, t: x + t, range(1, 5)))
print('-'*50)

# Callable: 호출 연산자. 즉, 호출가능한지 여부 확인
# callable() 메소드로 확인 가능
print(callable(str), callable(int), callable(var_func),
      callable(factorial), callable(10))

# 함수의 파라미터에 대한 정보 살펴보
from inspect import signature
sg = signature(var_func)
print(sg)
print(sg.parameters)
print('-'*50)

# partial 사용법 : 인수를 고정시키기 -> 콜백함수에 사용됨
# partial(함수, 고정시킬 인자)
from operator import mul
from functools import partial

# 인수 하나를 10으로 고정시키기
one_fix = partial(mul, 10)
# 10 인수를 고정시킨 채 2라는 추가 인수만 지정해주고 mul 연산 수행!
print(one_fix(2))
print([one_fix(i) for i in range(1, 11)])
# map 이용해보기
print(list(map(one_fix, range(1, 11))))
# filter는 참, 거짓을 판단해서 요소들을 필터링 하는 역할임!(map과는 다름!!)
print(list(filter(lambda x: x % 2, range(1, 11))))
# filter + map을 결합!!
print(list(map(one_fix, filter(lambda x: x % 2, range(1, 11)))))
print('-'*50)

# 인수 하나를 추가로 또 고정 시키기
double_fix = partial(one_fix, 2000)
print(double_fix()) # mul연산에 2개의 인수가 필요한데 이미 2개 인수 모두 고정시켰으므로 그냥 호출하면 됨!
# print(double_fix(4)) # 추가 인수를 넣어주면 에러 발생!


