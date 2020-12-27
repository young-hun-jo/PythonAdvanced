# Chapter05-04
# 파이썬 심화 -> 데코레이터!(데코레이터를 하기 위해서는 클로저가 필요!)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 공통 함수란.. 로킹, 일종의 프레임워크, 유효성 체크 가능
# 3. 조합해서 사용 용이

# 단점
# 1. 너무 남발하면 가독성 감소하기도 함..
# 2. 특정 기능에 한정된 함수는 굳이 데코레이터가 아닌 일반 단일 함수로 작성하는게 용이
# 3. 디버깅 불편.. 클로저 함수 타고 올라가야 함..

# 데코레이터 실습 - 특정 함수가 동작되고 종료되는 동안의 시간을 측정해보자
import time
# 우선, 클로저 함수 만들기
def perf_clock(func): # 함수를 인자로 전달 - 일급 객체의 특징
    # Free variable 구역
    def inner_func(*args): # 유동적인 인자를 위한 packing
        # 시작 time 측정
        st = time.perf_counter()
        result = func(*args)
        et = time.perf_counter()
        runtime = et - st
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f"{runtime :.5f} {name}({arg_str}) -> {result}")
        return result
    return inner_func

# 동작 시간을 측정할 함수 2가지 정의해주기
def sleep_func(seconds):
    time.sleep(seconds)
    return

def sum_func(*numbers):
    return sum(numbers)

# 1. 데코레이터를 사용하지 않고 호출하기
no_deco1 = perf_clock(sleep_func)
print("## None Decorator로 sleep_func 함수 동작 시간 출력 ##")
result1 = no_deco1(2)

no_deco2 = perf_clock(sum_func)
print("## None Decorator로 sum_func 함수 동작 시간 출력 ##")
result2 = no_deco2(1,2,3,4,5,6,7,8,9,10)
print("sum_func 함수 결과 :", result2)
print('-'*50)
# 2. 데코레이터 사용해보기
@perf_clock
def sleep_func(seconds):
    time.sleep(seconds)
    pass

@perf_clock
def sum_func(*numbers):
    return sum(numbers)
print("## Decorator로 sleep_func 함수 동작 시간 출력 ##")
result1 = sleep_func(2)
print("## Decorator로 sum_func 함수 동작 시간 출력 ##")
result2 = sum_func(1,2,3,4,5,6,7,8,9,)
print(result2)