# Chapter07-01
# AsyncIO : 코루틴에서 네트워크나 파일 쓰기와 같은 작업들을 따로 처리하도록 만든 라이브러리
# 사용할 함수가 blocking 함수라면 asyncIO를 쓰는 것보다 단일 쓰레드로 수행하는 것이 더 빨름
# 즉, 사용할 함수가 내부적으로 비동기로 구현되어 있어야 함. 마치 제네레이터 같이)
# 하지만 GIL을 우회하는 방법으로 멀티쓰레드를 사용함으로써 blocking 함수를 비동기로 구현 가능!

# 비동기 I/O을 코루틴으로 작업할 수 있도록 만들어놓은 라이브러리 = AsyncIO
# 제네레이터가 반복적인 객체를 반환해 사용
# Non-blocking 비동기를 사용
# 주로 웹서버, 네트워크, 데이터베이스 데이터 처리 등과 같은 병렬처리에 자주 사용

# Blocking I/O: 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 갖고 있음. 그래서 타 함수는 대기해야 함!
# Non-Blocking I/O: 호출된 함수(서브루틴)가 return(yield) 후 호출한 함수(메인루틴)에 제어권 전달-> 호출된 함수(서브루틴)는 하던 작업을 지속할 수 있음
# AsyncIO는 사용하려는 함수가 비동기로 구현되는 함수여야 함!

# 쓰레드 단점 : 디버깅, 자원 접근 시 race condition, 데드 락(교착 상태) 발생..그래서 코루틴을 사용하는데..
# 코루틴 장점 : 하나의 단일 쓰레드에서 여러가지 루틴이 실행됨 -> 락 관리 필요없음 -> 제어권을 주고받으면서 실행됨
# 코루틴 단점 : 하지만 사용하려는 함수가 비동기로 구현이 되어있거나 직접 비동기로 구현해주야야 함!

## 실습 예제 ##
import asyncio
import timeit # timeit의 정체는?
from urllib.request import urlopen
# urlopen은 block 함수임! 그래서 asyncIO를 원래는 사용할 수 없지만 코루틴과 쓰레드(또는 프로세스)를 결합해서 사용!
# => 즉, urlopen을 멀티쓰레드로 수행함으로써 각각의 쓰레드에서 수행하도록 하게 하면서 non-block의 효과가 발생하기 떄문에 이 때 asyncIO를 활용
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading

# 실행시작 시간
st = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습을 권장함!
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://wemakeprice.com/']

# urlopen은 non-blocking 함수 이기 때문에 멀티 쓰레드를 사용함. 그리고 asyncio에서 urlopen함수의 제어권을 yield로 넘기기

# 수행할 fetch 함수 정의 -> 해당 함수의 제어권을 주고받고 할 것이기 때문에 async를 넣어주어서 비동기 함수라는 것을 표시하자!
# 하나의 url당 하나의 스레드(executor)
async def fetch(url, executor):
    # 쓰레드명 출력 for debugging
    print('Thread name: ', threading.current_thread().getName(),
          'Start', url)
    # 실행 : 다른 애들이 끝날때까지 기다리고 요청을 할 것이기 때문에
    # run_in_executor(스레드, 수행할 작업(함수), )
    # block함수인 urlopen을 non-block으로 만들어주는 역
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread name: ', threading.current_thread().getName(),
          'Done', url)
    # 결과 반환 -> 작업 시작 순서와 끝나는 순서 달라지는 것을 확인 할 수 있음 => 비동기(우선 모든 url에 대해 다 요청한 다음 먼저 반응 오는 것부터 수행)
    return res.read()[:5]

# url들을 동시 수행하기 위해 쓰레드를 만들면서 asyncio로 넘겨주기
# 비동기 함수라는 것을 표시해주기 위해 def 앞에 async를 붙여주자!
async def main():
    # non-block이 되도록 하기 위해서 쓰레드 생성-> 쓰레드를 사용한 이유는 urlopen이 blocking 함수이기 때문!
    executor = ThreadPoolExecutor(max_workers=10)
    # future(할 작업들) 모아서(gather) 실행
    # url 하나당 하나의 쓰레드를 만들어야 함. ensure_future인자에 실행해줄 함수를 정의해줌!
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    # futures 끝날 때 결과를 모두 취합. await = yield
    # futures는 리스트이기 떄문에 unpacking(*)
    res = await asyncio.gather(*futures)
    print()
    print("Result: ", res)

# 메인함수 진입점
if __name__ == '__main__':
    # 루프 초기화 -> 제어권을 서로 주고받고 하겠다!
    loop = asyncio.get_event_loop()
    # 작업 완료때까지 루프가 계속되면서 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - st
    # 총 실행시간 출력
    print("Total Runtime :", duration)




















