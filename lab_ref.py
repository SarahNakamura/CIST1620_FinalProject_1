def student_score(student_num):
    score = input(f'Enter {student_num} score(s): ')
    score_list = score.split()
    if len (score_list) > student_num:
        score_list = score_list[:student_num]
    else:
        while len(score_list) < student_num:
            score = input(f'Enter {student_num} score(s): ')
            score_list = score.split()
    return score_list

def maximum(score1):
    y = 0
    for i in score1:
        ind_score = int(i)
        if ind_score > y:
            y = ind_score
    return y


num_students = int(input('Total number of students: '))
scores = student_score(num_students)
best = maximum(scores)
x = 0
student_number = 1
while x < num_students:
    a = int(scores[x])
    if a >= (best - 10):
        print(f'Student {student_number} score is {a} and grade is A')
    elif a >= (best - 20):
        print(f'Student {student_number} score is {a} and grade is B')
    elif a >= (best - 30):
        print(f'Student {student_number} score is {a} and grade is C')
    elif a >= (best - 40):
        print(f'Student {student_number} score is {a} and grade is D')
    else:
        print(f'Student {student_number} score is {a} and grade is F')
    x += 1
    student_number += 1
