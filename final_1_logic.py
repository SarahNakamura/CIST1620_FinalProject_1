from csv import *
from PyQt6.QtWidgets import *
from GPA import *

class Logic (QMainWindow, Ui_MainWindow):
    student_num = 0
    score_list = []
    def __init__(self):
        super.__init__()
        self.setupUi(self)

        self.submit_student_buttom.clicked.connect(lambda: self.student_submit())
        self.submit_final_button.clicked.connect(lambda:self.final_submit())



# returning a score list to use it to determining GPA
    def student_score(self):
        student_number = self.student_num
        #score = input(f'Enter {student_num} score(s): ')
        score_list = score.split()
        if len(score_list) > student_number:
            score_list = score_list[:student_number]
        else:
            while len(score_list) < student_number:
                score = input(f'Enter {student_number} score(s): ')
                score_list = score.split()
        return score_list

# determine the maximum score
    def maximum(score1):
        y = 0
        for i in score1:
            ind_score = int(i)
            if ind_score > y:
                y = ind_score
        return y

# determine the GPA
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

# submitting the student information
# count number of students as student information is submitted
    def student_submit(self):
        try:
            first_name = str((self.input_first.text()))
            last_name = str((self.input_last.text()))
            if self.freshman.isChecked():
                grade = 'Freshman'
            elif self.sophomore.isChecked():
                grade = 'Sophomore'
            elif self.junior.isChecked():
                grade = 'Junior'
            else:
                grade = 'Senior'
            midterm = int((self.input_midterm.text()))
            final = int((self.input_final.text()))
            final_score = (midterm + final)//2
            self.score_list.append(final_score)

            row = [last_name, first_name, grade, midterm, final, final_grade,gpa]
            with open('grade_info.csv', 'a', newline="") as info:
                write_info = writer(info)
                write_info.writerow(row)
                info.close()
        except:
            self.Error_message.insertPlainText(f'Please input the correct information.')
        self.student_num += 1
        self.clear()


# final submission/ display the GPA for each student
    def final_submit(self):
        self.student_score()
        self.maximum()
        self.GPA_display.insertPlainText(f'A')
        self.final_message.insertPlainText(f'Please check the csv file')
        self.clear()

    def clear(self):
        self.input_first.clear()
        self.input_last.clear()
        self.input_midterm()
        self.input_final()
        self.Error_message.clear()
        self.freshman.setChecked(True)





#creating a csv file for final grade report
def submit(self):
    first_name = self.