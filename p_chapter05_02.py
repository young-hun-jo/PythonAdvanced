# Chapter05-02
# 파이썬 심화 - 클로저 개념 이해

# 1. 파이썬 변수 범위(scope) 이해
# Ex1)
def func_v1(n):
    print(n)
    print(b)
# print(func_v1(10)) => 에러발생

# Ex2)
b = 20

def func_v2(a):
    print(a)
    print(b)
func_v2(10)

# Ex3)
b = 20
def func_v3(a):
    print(a)
    print(b)
    b = 40
    
# func_v3(10) => 에러발생! 함수 내부의 print(b)에서 b가 global 변수를 참조하고 있다고 선언을 해주지 않았기 떄문

# Ex4)
b = 20
def func_v4(a):
    print(a)
    global b
    print("전역변수 일때:",b)
    b = 40
    
func_v4(10)
print("지역변수 일때:", b)
print('-'*50)
# Closure 사용 이유 : 상태를 save 하기 위함!
# 메모리를 공유하지 않고 메세지 전달로 처리하기 위함. 결국 멀티 쓰레드(코루틴) 프로그래밍에 강함!
# 클로저는 공유하되 변경되지 않는(immutable) 것들로 적극적으로 사용됨 -> 함수형 프로그래밍

# 일반적인 누적합 구하기
print(sum(range(1,11)))
print()

# 누적 평균 구하는 Class 정의해보기
# 클래스의 매직 메서드 __call__은 클래스를 마치 함수(메소드)처럼 callable할 수 있음!!
class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, value):
        self._series.append(value)
        print(f"Series:{self._series}, Length:{len(self._series)}")
        # 누적 평균값 return
        return sum(self._series) / len(self._series)
# 클래스를 이용해 누적된 값 save
cls_averager = Averager()
result = cls_averager(10)
print("1번째:", result)

# 위에 save된 상태에서 누적시키고 평균구하기
result = cls_averager(20)
print("2번째:", result)
result = cls_averager(154)
print("3번째:", result)
result = cls_averager(256)
print("4번째:", result)

