"""
기능
10초 전 이동: "prev" 입력-> 동영상의 재생 위치 10초 전으로 이동
10초 후 이동: "next" 입력-> 동영상의 재생 위치를 10초 후로 이동
오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간인 경우 자동으로 오프닝 끝 위치로 이동

주어진 조건
영상 처음 위치: 0분 0초
영상 마지막 위치: 동영상 길이
이동 가능 10초 미만 경우: 0분 0초 or 동영상 길이

매개변수
동영상 길이: video_len (문자열)
기능 수행 직전 재생위치: pos (문자열)
오프닝 시작 시각: op_start (문자열)
오프닝 끝나는 시각: op_end (문자열)
사용자 입력: commands (1차원 문자열 배열)

반환값
입력 모두 끝난 후 동영상 위치: (형태) "mm:ss"

제한사항
video_len의 길이 = pos의 길이 = op_start의 길이 = op_end의 길이 = 5
video_len, pos, op_start, op_end는 "mm:ss" 형식으로 mm분 ss초를 나타냅니다.
0 ≤ mm ≤ 59
0 ≤ ss ≤ 59
분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타냅니다.
비디오의 현재 위치 혹은 오프닝이 끝나는 시각이 동영상의 범위 밖인 경우는 주어지지 않습니다.
오프닝이 시작하는 시각은 항상 오프닝이 끝나는 시각보다 전입니다.
1 ≤ commands의 길이 ≤ 100
commands의 원소는 "prev" 혹은 "next"입니다.
"""


"""
사용자 입력 -> 각 변수에 저장 (commands의 경우 split 후 list로 저장)
함수 시작
각 위치 변수 초단위로 합해 정수로 - 함수로 할까?
    가변인자로 위치 변수들 받음
    리스트 원소 for
        :를 기준으로 split, map int로 min과 sec 저장
        min*60+sec으로 대체해 저장
    리스트 반환
리스트 원소로 각 변수값 재할당
commands 원소 for
    재생위치 확인, 오프닝 구간일 시 오프닝 끝으로 이동
    prev인 경우와 아닌 경우로 나뉨
    prev일 때 10보다 작은 경우만 예외로 둠
    next일 때 video_len - 10보다 큰 경우만 예외로 둠
"""

def charToSec(*positions):
    new_positions = []
    for po in positions:
        min, sec = map(int, po.split(":"))
        new_positions.append(min*60+sec)
        
    return new_positions


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    sec_positions = charToSec(video_len, pos, op_start, op_end)
    video_len = sec_positions[0]
    pos = sec_positions[1]
    op_start = sec_positions[2]
    op_end = sec_positions[3]
    if (op_start <= pos <= op_end): pos = op_end
    
    for command in commands:
        if command == "prev":
            if pos <= 10: pos = 0
            else: pos -= 10
        elif command == "next":
            if pos >= (video_len - 10): pos = video_len
            else: pos += 10
        else:
            return False
        
        if (op_start <= pos <= op_end): 
            pos = op_end
    
    ans_min = pos//60
    ans_sec = pos%60
        
    answer = f"{ans_min:02d}:{ans_sec:02d}"
        
    return answer

videoLen = input("비디오 길이: ")
Pos = input("현재 위치: ")
opStart = input("오프닝 시작: ")
opEnd = input("오프닝 끝: ")
Command = list(input().split())
print(f"결과: {solution(videoLen, Pos, opStart, opEnd, Command)}")
