# chapter 01-02
# 가상환경 설정 테스트 코드
import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

# 타임 확인
print(type(pst))
print(type(ist))
print(datetime.now(pst))
print(datetime.now(ist))
