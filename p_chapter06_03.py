# Chapter06-03
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# yield : 메인 루틴 <-> 서브 루틴(상호작용..정보를 주고 받거니 함!)
# 코루틴 제어, 상태, 양방향 전송
# yield from 을 이용해 코드 간소화 가능
# Python3.5이상부터) def -> async / yield -> await(await는 StopIteration 자동처리해줌) 으로 대체 가능!

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름 제어)
# 코루틴 : 루틴 실행 중 중지하고 다른 루틴 실행 -> 동시성 프로그래밍, 그리고 멀티스레드에 비해 오버헤드 감소
# 코루틴은 단일 스레드에서 수행
# 스레드가 싱글 스레드 -> 멀티스레드로 가면 복잡해짐 -> 공유되는 자원(정보)기 교착 상태 발생. 또한 컨텍스트 스위칭 비용 발생으로 단일 스레드보다 속도 느릴 수 있음, 자원 소비 가능성 증가

# Coroutine Ex1)
def coroutine1():
    while True:
        # sub-routine area
        print(">> coroutine1 started")
        i = yield # 왼쪽은 메인->서브로 줄 값, 오른쪽은 서브->메인으로 줄 값
        print('>> coroutine1 received: {}'.format(i))

# 코루틴(일종의 제네레이터임) 선언
cr1 = coroutine1()
print(cr1, type(cr1)) # type : generator
# 코루틴 최초 실행
next(cr1) # 최초실행시 서브루틴의 yield 영역까지 실행된 후 대기상태!

# 메인 루틴에서 데이터(값) 전송!
cr1.send('this is a first data of main!')
cr1.send('this is a second data of main!')
print('-'*50)

# 잘못된 코루틴 사용법 -> 코루틴을 최초로 실행시킨 후 대기시켜야 함! 즉, 바로 메인->서브(코루틴)로 데이터 전송은 에러 발생
cr2 = coroutine1()
# cr2.send(1) -> 에러발생
cr2.send(None) # 하지만 메인->서브로 None을 send하면 자동으로 서브(코루틴)영역 최초 실행시켜줄 수 있음!
cr2.send(1)
print('-'*50)

# Coroutine Ex2)
# 코루틴 상태 종류 의미
# 1.GEN_CREATED : 처음 대기 상태
# 2.GEN_RUNNING : 실행 상태
# 3.GEN_SUSPENDED : 최초 실행 후 yield 대기 상태
# 4.GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print(">> coroutine2 started : {}".format(x))
    y = yield x # x는 서브루틴에서 제공, y는 메인루틴에서 제공할 값
    print(">> coroutine received : {}".format(y))
    z = yield x+y
    print(">> coroutine received : {}".format(z))

# 코루틴 상태 보기 위한 라이브러리 - generatorstate!
from inspect import getgeneratorstate
cr3 = coroutine2(10)
print(getgeneratorstate(cr3))
# 코루틴 최초 실행 -> 서브루틴이 담고있는 파라미터값 출력됨!
next(cr3)
print(getgeneratorstate(cr3)) # yield 대기 상태
print(cr3.send(20)) # 서브루틴에서 제공하는 x+y를 보려면 print()로 해주어야 함!
print(getgeneratorstate(cr3))
print('-'*50)

# Coroutine Ex3)
# 중첩 코루틴 처리
def generator1():
    for x in 'ABCD':
        yield x
    for y in range(1,5):
        yield y

t1 = generator1()
# next(t1) 만하면 아무것도 반환안함!
print(next(t1)) # 서브루틴에서 제공하는 yield 값을 보기 위해선 print!
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(list(t1)) # next() 메서드로 모든 요소 다 호출하고 나면 빈 리스트로 할당됨 왜? next() 호출 때마다 메모리에서 삭제되기 때문!
print('-'*50)

t2 = generator1()
print(list(t2))
print('-'*50)

# yield from 사용해보기
def generator2():
    yield from 'ABCD'
    yield from range(1,5)

t3 = generator2()
print(list(t3))




