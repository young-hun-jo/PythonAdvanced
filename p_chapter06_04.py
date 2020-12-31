# Chapter06-04
# Futures(동시성)은 여러개의 작업을 동시에 수행 또는 하나의 작업을 여러개로 분업 수행
# Coroutine은 하나의 흐름 속에서 서로 다른 여러개의 작업을 수행

# 비동기 작업 실행; 동기 작업이란, 예를 들어, A라는 작업이 1시간걸리고, B라는 작업이 1초가 걸리는데, 무조건 A작업이 끝나고 나서야 B작업을 수행하는 것을 말함
# 이와 반대로 비동기란, A, B 작업 둘 다 동시에 수행하는 것을 말함
# 비동기 작업 -> 지연시간(Block) CPU 및 리소스 낭비 방지 -> 주로 파일, 네트워크 I/O 관련 작업에 사용

# Futures : 비동기 실행을 위한 API를 고수준으로 작성함 -> 사용하기 쉽도록 개선
# concurrent의 futures 임포트해서 사용
# 1.멀티스레딩/멀티 프로세싱 API 통일 시킴 -> 사용하기 쉬움
# 2.실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가 등 동기화 코드 쉽게 작성 가능 -> Promise 개념

# GIL(Global Interpretor Lock) : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스할 경우 문제점이 발생할 것을 방지하기 위해 GIL 실행
# -> GIL의 역할 : 리소스 전체에 lock이 걸림, Context switching 비용 발생하기 때문에 lock 걸음!
# GIL을 우회하는 방법 : 꼭 필요한 방법은 멀티프로세싱을 이용하거나 CPython을 이용해 GIL이 걸리지 않도록 함(대신 동기화는 일일이 다 해주어야 함)

# 2가지 패턴
# concurrent.futures 사용법1
import os
import time
from concurrent import futures

WORK_LST = [1000, 10000, 100000, 1000000]

# 동시성을 수행할 합계 계산 함수 정의
# 누적 합계 함수(generator로 구현! 왜? 메모리에 다 담지 않도록 하기 위해서)
def sum_generator(n):
    cum_sum = sum(e for e in range(1, n+1))
    return cum_sum

# 동시성 수행하는 메인함수 정의
def main():
    # 수행할 작업들 count
    worker = min(10, len(WORK_LST)) # optional 방법임!
    # 동시성 수행 시작 시간
    start = time.time()

    # 동시성 수행 - futures의 스레드 이용! / ProcessPoolExecutor로 변경해 멀티프로세스 사용 가능!
    with futures.ThreadPoolExecutor() as executor:
        # map을 이용. map(수행할 작업의 함수, 작업들 담긴 iterable객체)
        result = executor.map(sum_generator, WORK_LST)

    # 동시성 수행 동안의 시간 계산
    end = time.time() - start
    # 시간, 결과 출력
    msg = "Result: {}\nRuntime: {: .2f}"
    print(msg.format(list(result), end))

# main 함수의 진입점(시작점)을 알려주어야 멀티프로세싱이 수행됨!
if __name__ == '__main__':
    main()


#################### 실행 시 위의 것 중 하나 주석처리 ####################
# ProcessPoolExecutor로 연습해보기
import time
from concurrent import futures

WORK_LST = [5050, 10000, 5000, 123]

# 평균값 구하는 함수
def avg_generator(n):
    n_sum = sum(e for e in range(1, n+1))
    return n_sum / n

# 동시성 수행할 메인 함수 정의
def main():
    # 시작 시간
    st = time.time()

    # 동시성 수행
    with futures.ProcessPoolExecutor() as executor:
        result = executor.map(avg_generator, WORK_LST)

    # 걸린 시간
    et = time.time() - st
    msg = "Result: {}\nRuntime: {: .2f}s"
    print(msg.format(list(result), et)) # result는 generator로 나옴!

if __name__ == '__main__':
    main()
