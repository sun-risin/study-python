"""
시간복잡도를 우선으로 생각해봐...

게임에 있는 붕대감기 기술
    t초동안 붕대감음, 1초마다 x만큼 체력 회복
    t초 연속 붕대 감는 데 성공 시 y만큼 추가 회복
    최대 체력보다 커지는 건 불가능
    
기술 쓰는 도중 공격 당하면 기술 취소, 당하는 동안 회복 불가
    기술 취소 or 기술 끝나면 붕대 감기 재사용 가능
    but 연속 성공시간 0으로 초기화됨
    
공격 당하면 정해진 피해량 만큼 현재 체력 줄어듦

체력 0 이하 되면 캐릭터 죽음, 회복 불가

붕대 기술 정보, 최대 체력, 공격 패턴 -> 캐릭터 끝까지 생존 가능?


매개변수
    bandage: 기술 시전 시간, 초당 회복량, 추가 회복량
    health: 최대 체력
    attacks: 공격 시간 및 피해량 (2차원 정수배열)
    
return: 모든 공격 끝난 직후 남은 체력
"""

"""
어떻게 할 것인가

첫 어택 -> 
    체력 변경
    이전 어택 시간에 어택 시간 저장
    attakcs에서 뺌(del(0))

attacks for O(n)
    다음 어택 전까지
        interval = 다음 어택 시간 - 이전 어택 - 1
        간격 * 초당 회복량
        (간격 // 시전 시간) * 추가 회복량
            두 개 더함, 
            현재 체력에 더한 후 만약 health보다 크면 health로 변경
    다음 어택 시 체력 변경
    이전 어택에 시간 저장
"""

def solution(bandage, health, attacks):
    answer = health
    bef_attack = 0
    
    # # 첫 어택 -> 불필요해짐 (bef_attack = 0)
    # answer -= attacks[0][1]
    # if answer <= 0 : return -1 # 0 이하되면 -1 return
    # bef_attack = attacks[0][0]
    # del attacks[0]
    
    # 어택 차례대로 진행
    for time, damage in attacks: # 언패킹으로 가독성 높임
        interval = time - bef_attack - 1
        if interval > 0:
            answer += (interval * bandage[1]) + ((interval // bandage[0]) * bandage[2]) # 공격 없는 동안 회복
            if answer > health: answer = health # 최대 체력은 못 넘김
        
        answer -= damage # 공격 받아서 깎임        
        if answer <= 0 : return -1 # 0 이하되면 -1 return
        
        bef_attack = time
        
    return answer

b1 =[5, 1, 5]
h1 = 30
a1 = [[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(b1, h1, a1))