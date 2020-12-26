# Chapter05-03
# 파이썬 심화 - 클로저 심화
# Closure 사용해보기 - outer function & inner function

def outer_func():
     series = [] # Free variable(자유 변수)
     def inner_func(value):
         series.append(value)
         print(f"Series:{series}, Length:{len(series)}")
         return sum(series) / len(series)
     # inner_func을 return 함으로써 상태를 계속 save!
     return inner_func

avg_closure1 = outer_func()
print(type(avg_closure1))
print("1번째 호출:", avg_closure1(10))
print("2번째 호출:", avg_closure1(20))
print("3번째 호출:", avg_closure1(55))
print('-'*50)

# Closure function inspection 해보기!
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) # 자유 변수 무엇인지 관찰
print(dir(avg_closure1.__closure__[0]))
print(avg_closure1.__closure__[0].cell_contents) # 자유 변수에 어떤 값이 들어있는지 관찰
print('-'*50)
print()

# 잘못된 Closure 사용법
def outer_func2():
    # Free variable 선언
    cnt = 0
    total = 0
    def inner_func2(value):
        cnt += 1 # inner_func2 외부에 있는 cnt, total 변수를 참조하지 못함!
        total += value
        return total / cnt
    return inner_func2

# wrong_closure = outer_func2()
# wrong_closure(10)

# 위 잘못된 방법 해결 방안
def outer_func3():
    cnt = 0 # Free variable 선언
    total = 0
    def inner_func3(value):
        # cnt, total이 inner_func3 함수 외부의 지역변수를 참조할 것을 선언!
        nonlocal cnt, total
        cnt += 1
        total += value
        return total / cnt
    return inner_func3

right_closure = outer_func3()
print("1번째 호출:", right_closure(10))
print("2번째 호출:", right_closure(20))
print("3번째 호출:", right_closure(55))
