"""
게시판 불량 이용자를 신고하고 처리 결과 메일로 발송하는 시스템

한 번에 한 명의 유저 신고 가능
    총 횟수 제한 X, 서로 다른 유저 계속해서 신고 가능
    한 유저 여러 번 신고 가능
        but 동일 유저에 대한 신고횟수는 1회로 처리
    
k번 이상 신고된 유저는 게시판 이용 정지
    해당 유저 신고한 모든 유저에게 정지 사실 메일로 발송

신고 내용들 취합해 마지막에 한꺼번에 이용 정지 및 메일 발송 진행


매개변수
    id_list = 이용자의 id 담긴 문자열 배열
    report = 각 이용자가 신고한 id 정보 담긴 문자열 배열
        A B 있으면 A가 B를 신고함
    k = 정지 기준 되는 신고횟수
    
return값
    각 유저별로 처리 결과 메일 받은 횟수 배열
        인덱스는 id_list에 따름
"""
"""
어떻게 할까?

신고 내역 -> set() -> 중복 제거된 집합으로 남음

신고 기록 딕셔너리
    키: 본인 이름
    값: 신고 기록 리스트
        본인 인덱스 -> 받은 횟수
        다른 인덱스 -> 했는지 여부 (1, 0)
        
        report 안에서 split해서 [0]은 rep [1]은 vic
        vic이 키인 곳
        본인 인덱스: vic 위치 값 +1
        다른 인덱스: rep 위치 값 1로
        
딕셔너리 값 리스트 내 본인 인덱스가 k 이상이면 
    다른 인덱스 중 1인것의 위치 +1 (answer 수정)
"""

def solution(id_list, report, k):
    user_cnt = len(id_list)
    answer = [0] * user_cnt
    
    report_set = set(report)  # 중복 제거
    report_dic = {name: [0] * user_cnt for name in id_list}
    
    for val in (report_set):
        rep, vic = val.split() # 제보자와 신고당한 사람
        
        report_dic[vic][id_list.index(vic)] += 1 # 본인 인덱스는 신고당한 횟수
        report_dic[vic][id_list.index(rep)] = 1  # 다른 인덱스는 본인을 신고한 여부
    
    for key in report_dic:
        vic_idx = id_list.index(key)
        if report_dic[key][vic_idx] >= k:  # 정지 될 사람이라면
            report_dic[key][vic_idx] = 0
            answer = [val[0] + val[1] for val in zip(answer, report_dic[key])]
    
    return answer

id1 = ["muzi", "frodo", "apeach", "neo"]
rep1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2

id2 = ["con", "ryan"]
rep2 = 	["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id1, rep1, k1))
print(solution(id2, rep2, k2))