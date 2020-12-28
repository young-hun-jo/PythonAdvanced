# Chapter06-01
# 병행성(Concurrency)
# iterator, generator
# generator는 iterable한 객체를 할당한 iterator를 하나씩 반환할 수 있는 것을 의

# 파이썬 반복 가능한 타입
# collections의 모든 자료구조, text file, list, dict, set, tuple, unpacking, *args, **kwargs

# 반복 가능한 이유는 뭘까? => 바로 __iter__ 이라는 매직 메소드 덕분!
string = 'ABCDEFGHIJKLMNOP'
print(dir(string)) # __iter__ 매직메소드 존재
for s in string:
    print(s)
print('-'*50)

# while 반복문 사용
w = iter(string)
print(w) # 문자열 iterator
while True:
    # try~except 구문으로 예외처리
    try:
        print(next(w))
    except StopIteration:
        print("Index is out of range!")
        break
print('-'*50)

# iterable한 자료구조인지 확인하는 방법들
# 1. dir로 확인하고 __iter__ 직접 눈으로 찾기
print(dir(w))
# 2. hasattr 메소드 사용
print(hasattr(w, '__iter__'))
# 3. collections의 abc(abstraction) 메소드 사용
# isinstance 메소드 : 어떤 속성을 상속받고 있는지 여부 확인 가능
from collections import abc
print(isinstance(w, abc.Iterable)) # w 즉, iterator라는 일종의 클래스가 abc.Iterable 속성을 상속받고 있는지 확인!
print('-'*50)

# 실습 : 문장을 공백으로 구분하는 클래스 만들기
# 1. 단순히 next 매직 메서드를 수정해 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # index가 out of range할 경우를 대비해 예외 처리
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("** Index is out of range!! **")
        # 문장의 다음 단어로 이동하기 위해 index + 1
        self._idx += 1
        return word

    def __repr__(self):
        return "Word Splitter: (%s)" % (self._text)

ws1 = WordSplitter('가지 많은 나무에 바람 잘 날 없다')
# print(ws1.__next__()) # 이렇게 호출해도 되긴 함
print(next(ws1))
print(next(ws1))
print(next(ws1))
print(next(ws1))
print(next(ws1))
print(next(ws1))
print(next(ws1))
# print(next(ws1)) => 예외처리 에러 메세지 발생
print('-'*50)

# 2. Generator인 __iter__ 사용해서 구현
# Generator는 데이터 양이 증가함에 따라 메모리 사용량이 증가할 때 사용 권장
# 단위 실행이 가능한 코루틴 구현과 연동
# 데이터를 한 번에 메모리에 올리지 않음. 즉, 작은 메모리 조각으로 사용 가능

class WordSplitter:
    def __init__(self, text):
        self._text = text.split(' ')

    # iter라는 Generator로 만들자!
    # iter은 내부적으로 예외처리까지 자동으로 해줌!
    def __iter__(self):
        for word in self._text:
            yield word

    def __repr__(self):
        return "Generator WordSplitter: (%s)" % (self._text)

ws2 = WordSplitter('가지 많은 나무에 바람 잘 날 없다')
ws2 = iter(ws2) # iter 매직메소드로 generator 할당 해주기(1번 실습과 차이점!)
print(ws2)
print(next(ws2)) # generator도 하나씩 출력은 next 메소드로 함
print(next(ws2))
print(next(ws2))
print(next(ws2))
print(next(ws2))
print(next(ws2))
print(next(ws2))
# print(next(ws2)) -> 예외 처리 에러 발생


