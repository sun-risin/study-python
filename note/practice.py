# 각 날마다 노트한 내용을 종합해 문제 연습하는 파일

# 0815 - all, any, enumerate, zip 
"""
두 명의 학생 점수 리스트가 주어짐.
두 학생 모두 50점 이상인 과목이 하나라도 있는지, 모든 과목에서 두 학생 다 50점 이상인지
50점 미만 점수가 있다면 그 과목의 인덱스 반환
"""
student1 = [60, 45, 80]
student2 = [70, 55, 40]
def sol(stu1, stu2):
    
    if all((sc1 >= 50 and sc2 >= 50) for sc1, sc2 in zip(stu1, stu2)): # 모든 과목에서 두 학생 다 50점 이상
        return True, True, []
    else:   # 두 번째 리턴값은 False
        under_fifty = [idx for idx, val in enumerate(zip(stu1, stu2)) if (val[0] < 50 or val[1] < 50)]
        if any((sc1 >= 50 and sc2 >= 50) for sc1, sc2 in zip(stu1, stu2)): # 두 학생 모두 50점 이상인 과목 존재
            return True, False, under_fifty
        else:
            return False, False, under_fifty
        
print(sol(student1, student2))


# 훨씬 깔끔하고 가독성이 좋다... zip도 한 번만 하면 됨
def gpt_sol(stu1, stu2):
    under_fifty = []
    any_ok = False
    all_ok = True
    
    for idx, (sc1, sc2) in enumerate(zip(stu1, stu2)):
        if sc1 >= 50 and sc2 >= 50:
            any_ok = True
        else:
            all_ok = False
            under_fifty.append(idx)
    
    return any_ok, all_ok, under_fifty