# Chapter03-02
# 파이썬 심화
# Special Method(Magic Method) = 이미 built-in 되어 있는 메소드들 의미!
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직 메소드 클래스 심화 예제
# 벡터 연산 클래스 만들기
import math

class Vector(object):
    def __init__(self, *args): # args는 내맘대로 네이밍 변경 가능
        '''Create a vector, example: v = Vector(5, 10)'''
        # args는 tuple 형태로 받아들여짐
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    # Class 할당한 객체 호출시 나오게 되는 인스턴스 정보
    def __repr__(self):
        '''Return the vector information'''
        return "Vector: (%r, %r)" % (self._x, self._y)
    # Vector 더하기 연산
    def __add__(self, inst):
        result = (self._x + inst._x, self._y + inst._y)
        return result
    # Vector 빼기 연산
    def __sub__(self, inst):
        result = (self._x - inst._x, self._y - inst._y)
        return result
    # Vecotr 곱하기 연산
    def __mul__(self, const):
        result = (self._x * const, self._y * const)
        return result
    # 두 벡터들 간의 유클리디안 거리 구하기
    def euclidian_dist(self, inst):
        x, y = pow((self._x - inst._x),2), pow((self._y - inst._y),2)
        dist = math.sqrt(x + y)
        return dist




vec1 = Vector(5, 10)
vec2 = Vector(3, 7)
vec3 = Vector()
print(vec1)
print(vec2)
print(vec3)
print('-'*50)
print("Add: ", vec1 + vec2)
print("Sub: ", vec1 - vec2)
print("Mul: ", vec1 * 3)
print("Euclidian Distance: ", Vector.euclidian_dist(vec1, vec2))

