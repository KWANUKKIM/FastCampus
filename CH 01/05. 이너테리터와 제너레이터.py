
"""
이너레이터
집합에서 값을 차례대로 꺼낼 수 있는 객체(Object)를 말합니다.
for 문을 순회할 수 있는 객체
사용이유?
숫자가 아주 많을 경우 미리 만들어 놓는 것 보다
그때그때 필요할 때 값을 뽑아 사용하고 싶은 경우가 대부분의 상황에서 효율적(메모리)
반복 가능(iterable)객체에서만 사용 가능
iter()로 반곡 가능 객체 변환
next()로 다음 값 뽑기
한번 반복하면 다시 사용될 수 없음.
"""



#example 1
for a in[1,2,3]:
    print(a)



#example 2
a = [1, 2, 3, 4]
a = iter(a)
print(iter(a))
print(a.__next__())
print(next(a))
print(next(a))
print(a.__next__())





