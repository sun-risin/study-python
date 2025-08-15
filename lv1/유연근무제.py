"""
매개변수
schedules: 1차원 정수 배열 (희망시각 리스트, i+1번째 직원의 희망)
timelogs: 2차원 정수 배열 (일주일간 출근 시간, i+1번째 직원의 j+1일차)
startday: 이벤트 시작 요일 정수 (1~7 -> 월~일)

시*100+분 으로 시각 표현.

문제
희망 출근 시각+10분까지 출근하면 늦지 않은 걸로 간주
일주일동안 늦지 않은 직원에게 상품.
토, 일 출근은 출근 이벤트에 영향X
상품 받을 직원의 수?
"""

"""
시각은 다루기 쉽게 분단위 변환하여 늦지 않았는지 확인 -> check_workTime(sch, log)
    시: 시각//100, 분: 시각%100
    시각: 시*60+분
    log-sch <= 10 이면 지각X(true), 아니면 지각(false) return

solution?
    prize = 0
    for i in range(len(schedule))
        ok = 0
        for j in range(len(timelogs[i]))
            if (j == 6-startday) or (j == 7-startday) or (j == 6 and 6-startday == -1) 
                토, 일은 제외. 일요일의 경우 -1, 0이라서 -1일 경우를 따로 적어줌
                continue
            elif (check_worktime(schedule[i], timelogs[i][j]))
                    ok += 1
        
        if ok == 5 : prize += 1 # 평일 동안 지각 X, 상품
        
    return prize
"""

def check_workTime(sch, log):
    sch_h, sch_m = sch//100, sch%100
    log_h, log_m = log//100, log%100
    
    sch = sch_h*60 + sch_m
    log = log_h*60 + log_m
    
    return (log-sch <= 10)

def solution(schedules, timelogs, startday):
    prize = 0
    sat, sun = (6-startday)%7, (7-startday)%7 # 프로그래머스 참고. 이게 더 깔끔! 원형큐 생각은 했는데 적용을 못햇다...
    
    for i in range(len(schedules)):
        ok = 0 # i+1번째 직원의 지각 안 한 날짜 수
        for j in range(len(timelogs[i])):
            if (j == sat) or (j == sun): # 프로그래머스 참고... 
                continue
            elif check_workTime(schedules[i], timelogs[i][j]):
                ok += 1
            else: # 평일 한 번이라도 지각하면 제외됨
                break
        
        if ok == 5 : prize += 1
        
    return prize


sch1 = [700]
log1 = [[710, 2359, 1050, 700, 650, 631, 659]]
start1 = 5
sch2 = [730, 855, 700, 720]
log2 = [[710, 700, 650, 735, 700, 931, 912],
        [908, 901, 805, 815, 800, 831, 835],
        [705, 701, 702, 705, 710, 710, 711],
        [707, 731, 859, 913, 934, 931, 905]]
start2 = 1

print(f'res1: {solution(sch1, log1, start1)}')
print(f'res2: {solution(sch2, log2, start2)}')



# gpt가 코드리뷰 해줌
def to_minutes(t):
    return (t // 100) * 60 + (t % 100)

def gpt_check_workTime(sch, log):
    return to_minutes(log) - to_minutes(sch) <= 10

def gpt_solution(schedules, timelogs, startday):
    weekend = {(6 - startday) % 7, (7 - startday) % 7}
    prize = 0
    
    for sch, logs in zip(schedules, timelogs): # 동일 인덱스끼리 묶여 순회
        if all(i in weekend or gpt_check_workTime(sch, log) for i, log in enumerate(logs)):
            prize += 1
    return prize

"""
gpt_check_workTime 내에서 분 변환을 따로 함수로 뺌 (가독성 높임)

gpt_solution 내부
    weekend 집합을 만들어서 주말인 날짜를 묶어 관리
    
    zip() -> 튜플, 리스트 등을 같은 인덱스끼리 묶어 동시 순회 / 반환: 튜플 형태
        => schedule에 쓸 i가 불필요해짐, 생략 가능
        => sch: 한 직원의 희망 시각, 정수 / logs: 해당 직원의 출근 기록, 1차 정수 리스트
        
    all() -> 괄호 안 내용 모두 True일 때 True.
        주말일 땐 그냥 통과, 이외에는 gpt_check_workTime->true여야 함
        
    enumerate() -> 리스트 인덱스 순으로 인덱스, 값 튜플 반환함
        logs 내 인덱스 -> 출근 일차 -> i, 주말인지 확인할 때 쓰임
        logs 값 -> 출근 기록 -> sch 함께 gpt_check_workTime 매개변수

변화: 가독성 개선
"""

print(f'gpt_res1: {gpt_solution(sch1, log1, start1)}')
print(f'gpt_res2: {gpt_solution(sch2, log2, start2)}')