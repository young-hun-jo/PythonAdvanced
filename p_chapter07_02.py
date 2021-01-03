#Chapter07-02
#asyncio 스크래핑 실습
import asyncio
import timeit
import threading
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 실행 시작 시간
st = timeit.default_timer()
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://www.inflearn.com/']

# 작업 내용인 비동기 fetch() 함수 정의 -> url과 url이 할당된 쓰레드 파라미터로 입력!
async def fetch(url, executor):
    # 수행중인 쓰레드 공간 이름 출력
    print('Thread Name:', threading.current_thread().getName(),'Start:', url)
    # 각 쓰레드에서 urlopen 함수를 수행하면서 loop로 주고받는 작업을 코루틴으로 await(yield)
    res = await loop.run_in_executor(executor, urlopen, url)
    # BeautifulSoup를 이용해서 원하는 텍스트 크롤링: res.read() == res.content와 동일!
    soup = BeautifulSoup(res.read(), 'html.parser')
    result_data = soup.find('title').get_text()
    print('Thread Name:', threading.current_thread().getName(), 'Done', url)
    return result_data

# 동시성 수행하는 비동기 메인함수 정의
async def main():
    # urlopen은 Blocking 함수이기 때문에 이를 위한 멀티쓰레드를 만들자
    executor = ThreadPoolExecutor(max_workers=10)
    # 하나의 url에 하나의 쓰레드가 할당되도록 하고 수행할 작업함수 fetch()를 할당해 작업 수행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    # 수행한 작업의 결과들 모아서 취합한 후 결과들 리턴 -> await(yield) 사용해서 코루틴 수행!
    res = await asyncio.gather(*futures)
    print()
    print('취합된 결과들:', res)

# 진입할 메인 함수 설정
if __name__ == '__main__':
    # loop 초기화
    loop = asyncio.get_event_loop()
    # 동시성 수행하는 메인 함수 작업 완료까지 기다리기
    loop.run_until_complete(main())
    # 수행시간 계산
    duration = timeit.default_timer() - st
    print('Total Runtime :', duration)