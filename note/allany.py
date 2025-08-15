"""
any() : 하나라도 True인게 있으면 True
all() : 모두 True여야 True 반환
"""

# 사용했던 사례 - 유연근무제, pcce_10

# 연습
# any - 리스트 내 음수가 하나라도 있는지 확인
nums = list(map(int, input().split()))
def sol1(nums):
    return any(num < 0 for num in nums)
print(sol1(nums))

# all - 학생들 시험 점수 모두 60점 이상인지 확인
scores = list(map(int, input().split()))
def sol2(scores):
    return all(score >= 60 for score in scores)
print(sol2(scores))