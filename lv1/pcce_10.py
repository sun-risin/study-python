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
    아니라면 원래 위치 X로 표시 후 다시 동일 행 내에서 첫 줄을 진행 (행 내 -1 길이가 돗자리크기인 곳이 없을 때까지)
전체 park를 다 봐도 가능하지 않다면 해당 크기는 mats에서 제외
"""

"""
any() : 하나라도 True인게 있으면 True
all() : 모두 True여야 True 반환
"""

def possibleLength(r, cnt, park): # cnt 길이 돗자리 가능 여부 알아보기
    p_row = park[r]
    p_col = len(p_row)

    for start_col in range(p_col - cnt + 1):  # 가능한 시작 열만 탐색
        ok = True
        # 첫 줄부터 cnt줄까지 확인
        for i in range(r, r + cnt):
            if any(park[i][j] != "-1" for j in range(start_col, start_col + cnt)): # 하나라도 -1 아닌 곳 있으면 X
                ok = False
                break
        if ok: return True

    return False


def solution(mats, park):
    answer = 0 # 반환값 초기화
    
    rows, cols = len(park), len(park[0]) # park의 행과 열 길이
    for mat in mats:
        if mat > min(rows, cols): mats.remove(mat) # park보다 큰 돗자리는 제외
    
    while mats:
        answer = max(mats)

        for r in range(rows - answer + 1):  # 시작 행, 남은 행 개수가 돗자리 길이보다 짧기 전까지
            if possibleLength(r, answer, park): return answer
        mats.remove(answer)

    return -1


m = [5, 3, 2]
p = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
     ["A", "A", "-1", "B", "B", "B", "B", "-1"],
     ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
     ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

print(f"결과: {solution(m, p)}")