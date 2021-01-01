# Chapter06-04
# Futures.concurrent 사용
# 2가지 패턴 실습
# 1)concurrent.futures.map => 이전 챕터에서 실습
# 2)concurrent.futures wait, as_completed

# wait, as_completed가 필요한 이유: 각 작업마다 완료되는 시간이 다르며 적게 소요되는 작업은 길게 소요되는 작업이 완료되까지 계속 대기해야 하는 문제 발생..이를 해결하기 위함
# 2)-1. wait: timeout을 설정할 수 있으며 일정 시간이 초과되는 작업을 실패로 간주하고 다른 작업들을 수행
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

# 수행할 작업 리스트 정
WORK_LST = [1000000, 1000000, 100000000, 1000000000]

# 누적합 구할 함수 정의
def sum_generator(n):
    res = sum(e for e in range(1, n+1))
    return res

# 동시성 수행할 메인함수 정의
# 우선 결정할 사안 -> 멀티스레드 / 멀티프로세싱
# 다음 결정할 사안 -> map / wait / as_completed
def main():
    # 수행할 작업들 count
    worker = min(10, len(WORK_LST))
    # 동시성 수행 시작 시간
    st = time.time()

    # 수행할 작업(future이라고함)들을 담을 빈리스트 정의
    futures_lst = []
    # 동시성 수행 - wait을 이용: 작업들 submit,스케쥴링 후 wait 수행!
    with ThreadPoolExecutor() as executor:
        # 수행할 작업들 loop
        for work in WORK_LST:
            # 수행할 각 작업에 대한 future 반환
            future = executor.submit(sum_generator, work)
            # future들 스케쥴링
            futures_lst.append(future)
            # 스케쥴링 확인
            print('Scheduled for {}: {}'.format(work, future))

        # wait으로 타임아웃 설정 후 동시성 수행
        result = wait(futures_lst, timeout=6)
        # 설정한 타임아웃 내 수행된 작업들(done) 출력
        print('* Completed Task:'+ str(result.done)) # result.done은 set(집합) type! = iterable 객
        # 타임아웃 초과되어 실패된 작업들(not_done) 출력
        print('* Over timeout Task:'+str(result.not_done))
        # 수행된 작업들의 결과물 출력
        print([res.result() for res in result.done])

        '''
        # as_completed: 수행 시간이 적게 걸리는 작업들부터 우선 반환됨!
        for future in as_completed(futures_lst):
            # 각 작업들의 결과물 할당(적게 걸리는 작업들 부터!)
            result = future.result()
            # 작업들이 완료되었는지 확인
            done = future.done()
            # 작업들이 취소되었는지 확인
            cancelled = future.cancelled()
            print('Future Result:{}, Done:{}'.format(result, done))
            print('Future Cancelled:{}'.format(cancelled))
        '''
    # 시성 수행 완료 시간
    end = time.time() - st
    print(f"Runtime: {end :.2f}")

if __name__ == '__main__':
    main()