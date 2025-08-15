"""
enumerate() -> 리스트 순회하며 (인덱스, 값) 튜플 반환
"""

# 사용 사례 - 유연근무제, 가장많이받은선물

# 연습
# 문자열에서 대문자의 인덱스를 모두 반환하는 함수
s = input()
def sol(s):
    small_s = s.lower()
    res = []
    for idx, val in enumerate(s):
        if (small_s[idx] != val):
            res.append(idx)
            
    return res
print(sol(s))