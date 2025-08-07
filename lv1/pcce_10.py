"""
돗자리 - 정사각형

매개변수
돗자리들의 한 변의 길이들: mats (정수 리스트)
현재 공원의 자리 배치도: park (2차원 문자열 리스트)

반환값
배치 가능한 가장 큰 돗자리의 한 변의 길이

제한사항
1 ≤ mats의 길이 ≤ 10
1 ≤ mats의 원소 ≤ 20
mats는 중복된 원소를 가지지 않습니다.
1 ≤ park의 길이 ≤ 50
1 ≤ park[i]의 길이 ≤ 50
park[i][j]에 돗자리를 깐 사람이 없다면 "-1",
사람이 있다면 알파벳 한 글자로 된 값을 갖습니다.
"""

"""
rows, cols 값 해놓음 (각각 len(park), len(park[0]))
min(rows, cols)보다 큰 값 mats에서 제외 (공원 크기보다 큼)

-1의 길이가 돗자리 크기인 곳이 존재하는 행일 때, 그 시작위치를 알아냄
    해당 행에서 +돗자리크기-1 위치의 행까지 같은 시작위치에서 돗자리 크기만큼 모두 -1이라면 True
    아니라면 원래 위치 X로 표시 후 다시 첫 줄을 진행
전체 park를 다 봐도 가능하지 않다면 해당 크기는 mats에서 제외
"""

def possibleLength(li, cnt, park, row): # cnt 길이 돗자리 li에 가능 여부
    li_str = "".join(li)
    cols = len(park[0])
    
    if ("-1"*cnt in li_str):
        for c in range(cols):
            check = [col[c] for col in park[row:]]
            if (("-1"*cnt) in "".join(check)): return True
            else: return False
    else:
        return False 


def solution(mats, park):
    answer = 0 # 반환값 초기화
    
    rows, cols = len(park), len(park[0]) # park의 행과 열 길이
    mats = [mat for mat in mats if mat <= min(rows, cols)]

    while len(mats) != 0:  # 모든 돗자리 확인
        answer = max(mats) # 큰 돗자리부터
        
        for r in range(rows):
            if possibleLength(park[r], answer, park, r):
                return answer
            else:
                if (rows - r -1 < answer):
                    mats.remove(answer)
                    break
                continue

    return -1


m = [5, 3, 2]
p = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
     ["A", "A", "-1", "B", "B", "B", "B", "-1"],
     ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
     ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

print(f"결과: {solution(m, p)}")