"""
1~n: 택배상자 번호
w: 한 줄에 쌓을 상자 개수
-> 하다가 짝수 번째 높이에서는 <-로 쌓음

정리
    번호/w
    몫: 아래에서 몇 번째 행?(idx)
    나머지: 그 줄에서 몇 번째로 쌓음?
        -> 1이거나 0?
            몫이 홀수이면 몫이 홀수이면서 나머지가 0이거나 1인 개수
            몫이 짝수이면 몫이 짝수이면서 나머지가 0이거나 1인 개수
            
        -> 이외로 몫 홀수이면 reverse, 즉 짝수랑 같은 열인지 보려면
            w+1-나머지 해야 함
    
    번호/w 의 몫과 나머지 구하고,
        나머지가 1이거나 0인 경우 따로 하고
        이외에는
            n보다 작은 숫자 중 몫보다 큰 숫자의 몫을 가지면서 나머지가 같은(몫 홀수일 경우 주의) 값의 개수 구함
"""

def RowAndCol(num, w):
    row = num//w
    if (row%2 != 0) and (num%w not in [0, 1]):            
        col = (w+1) - (num%w)
    else:
        col = num%w
        
    return row, col

def solution(n, w, num):
    answer = 1
    
    if w == 1: return (n - num) + 1
    
    row_idx, col_idx = RowAndCol(num, w)
    
    if col_idx in [0, 1]:
        for i in range(num+1, n+1):
            r, c = RowAndCol(i, w)
            if (row_idx%2 == r%2) and (c in [0, 1]):
                answer += 1
    
    else:
        for i in range((row_idx+1)*w +1, n+1):
            r, c = RowAndCol(i, w)
        
            if col_idx == c: 
                answer += 1
            
    return answer

n1 = 22
w1 = 6
num1 = 8

n2 = 15
w2 = 3
num2 = 6

print(solution(n1, w1, num1))
print(solution(n2, w2, num2))




""" 프로그래머스와 gpt 참고하여 셀프 코드리뷰함 """

def RowAndCol2(num, w):
    # 인덱스를 0부터 세는 방식, 나머지가 0인 경우 따로 처리 안해줘도 됨
    row = (num - 1) // w
    col = (num - 1) % w + 1 
    
    if (row%2 != 0): # 홀수일 때는 역순
        col = w - col + 1
        
    return row, col


def sol2(n, w, num):
    top_row, top_col = RowAndCol2(n, w)    
    num_row, num_col = RowAndCol2(num, w)
    
    answer = top_row - num_row + 1
    
    if n%w != 0:
        if top_row%2 == 0 and num_col > top_col:
            answer -= 1
        elif top_row%2 != 0 and num_col < top_col:
            answer -= 1
    
    return answer

print(sol2(n1, w1, num1))
print(sol2(n2, w2, num2))