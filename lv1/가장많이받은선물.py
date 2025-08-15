"""
총 1시간 22분 걸림
"""

"""
friends => sort. 사전순 정렬됨

친구 별로 선물 준 개수 리스트 만듦. 2차원 리스트로 관리 
give[i][j] -> friends 내 i번째 인덱스 친구의 j번째 인덱스 친구에게 준 선물 수
give = [[0]*len(friends)] * len(friends) -> 이러면 얕복 돼서 문제가 생김
깊복 하기!!
    [[0] * friend_cnt for _ in range(friend_cnt)]

누가 더 많이 줬는지: 서로의 인덱스에 해당하는 값의 크기 비교

선물 지수: 본인 인덱스 제외 모든 인덱스 합 - 다른 give 행들의 본인 인덱스 합
    => 이걸 본인 인덱스에 채우기
"""

"""
선물지수 구하기
    for i in range give:
        giving_sum = sum(give[i])
        receive_sum = 0
        
        for j in range give:
            if i == j (본인): continue
            receive_sum += give[j][i]
        
        give[i][i] = giving_sum - receive_sum

선물 준 리스트 구하기
    for i in range friends:
        for j in range friends:
            if i == j (본인) : continue
            
            give[i][j] = gifts.count(f"{friends[i]} {friends[j]}")

solution
    friends.sort()
    give = [[0]*len(friends)] * len(friends)
    
    선물 준 리스트 구하기(friends, gifts, give)
    
    선물 지수 구하기(give)
    
    max_gift = 0
    
    for i in range give:
        will_receive = 0
        for j in range give:
            if i == j (본인): continue
            if give[i][j] > give[j][i]:
                will_recieve += 1
            elif give[i][i] > give[j][j]:
                will_recieve += 1
        
        max_gift = max(max_gift, will_recieve)
"""

def gift_idx(give):  # 선물 지수 구한 후 give 내 본인 인덱스에 저장   
    give_cnt = len(give) 
    for i in range(give_cnt):
        giving_sum = sum(give[i])
        receive_sum = 0
        
        for j in range(give_cnt):
            if i == j: continue
            receive_sum += give[j][i]
        
        give[i][i] = giving_sum - receive_sum
        

def cal_give(friends, gifts, give): # give 리스트 구성 
    # 바꾼 이후 시간복잡도 변화: f^2*g -> g 
    
    # idx: 각 이름에 따른 give 내 첫 번째 인덱스 (행 순서)
    # enumerate: 리스트에서 인덱스, 값 반환
    idx = {name: i for i, name in enumerate(friends)}
    
    for record in gifts:
        giver, receiver = record.split() # 공백 기준으로 나눠 준 사람, 받은 사람
        give[idx[giver]][idx[receiver]] += 1 # 이름에 해당하는 인덱스 찾아가 +1
            
            
def solution(friends, gifts):
    friend_cnt = len(friends)
    give = [[0] * friend_cnt for _ in range(friend_cnt)] # 깊은복사 해 0으로 이루어진 리스트들 만들기
    
    cal_give(friends, gifts, give)
    
    gift_idx(give)
    
    max_gift = 0
    
    for i in range(friend_cnt):
        will_receive = 0
        for j in range(friend_cnt):
            if i == j: continue
            
            if give[i][j] > give[j][i]: # i친구가 더 많이 줌
                will_receive += 1
                
            # not(give[j][i]~) 는 give[i][j] == give[j][i]와 같은 의미가 됨. -> 가독성 개선
            elif give[i][j] == give[j][i] and give[i][i] > give[j][j]: # i친구 선물지수가 더 큼
                will_receive += 1
        
        max_gift = max(max_gift, will_receive)
        
    return max_gift

# 최종 시간 복잡도 변화: f^2 * g -> f^2 + g

f1 = ["muzi", "ryan", "frodo", "neo"]
g1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

f2 = ["joy", "brad", "alessandro", "conan", "david"]
g2 = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

f3 = ["a", "b", "c"]
g3 = ["a b", "b a", "c a", "a c", "a c", "c a"]

print(f'res1: {solution(f1, g1)}')
print(f'res2: {solution(f2, g2)}')
print(f'res3: {solution(f3, g3)}')