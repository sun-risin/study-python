"""
zip() -> 튜플, 리스트 등을 같은 인덱스끼리 묶어 동시 순회
    반환: 튜플 형태
"""

# 사용 사례 - 유연근무제

# 연습
# 두 리스트의 원소를 서로 곱한 결과 리스트를 반환
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def sol(a, b):
    res = []
    for i, j in zip(a, b):
        res.append(i*j)
        
    return res

print(sol(a, b))

# 리스트 컴프리헨션으로 더 간단히 가능하다 알려줌
def gpt_sol(a, b):
    return [i*j for i, j in zip(a, b)]