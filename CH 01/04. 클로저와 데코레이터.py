"""
클로저(Closure)
함수 안의 함수를 결과로 반환할 때, 그 내부 함수를 클로저(Closure)라고 합니다.
사용되는 곳
콜백(Callback) 함수에 사용
함수의 순차적 실행
데코레이터 함수
"""

def mul3(n):
    return n*3

print(mul3(3))
print(mul3(5))






