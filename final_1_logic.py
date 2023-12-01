from csv import *
from PyQt6.QtWidgets import *
from GPA import *

class Logic (QMainWindow, Ui_MainWindow):
    score_list = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_student_buttom.clicked.connect(lambda: self.student_submit())
        self.submit_final_button.clicked.connect(lambda: self.final_submit())

# submitting the student information
# count number of students as student information is submitted
    def student_submit(self):
        self.write_csv_file() # input student information
        self.clear() # clear student information input

# final submission/ display the GPA for each student
    def final_submit(self):
        self.GPA_display.insertPlainText(f'!!!')
        self.final_message.insertPlainText(f'Please check the csv file')
        self.clear()

# retrieve student information from input \
# create a list of retrieved information(fist,last,school year,midterm,final,average)
# append average score to a separate list
    def retrieve_information(self):
        try:
            first_name = str((self.input_first.text()))
            last_name = str((self.input_last.text()))
            if self.freshman.isChecked():
                school_year = 'Freshman'
            elif self.sophomore.isChecked():
                school_year = 'Sophomore'
            elif self.junior.isChecked():
                school_year = 'Junior'
            else:
                school_year = 'Senior'
            midterm = int((self.input_midterm.text()))
            final = int((self.input_final.text()))
            average = (midterm + final)//2
            self.score_list.append(average)
            return last_name, first_name, school_year, midterm, final
        except:
            self.Error_message.insertPlainText(f'Please input the correct information.')

# determine the GPA and grade in letter
    def determine_grade(self):
        info = self.retrieve_information()
        average = (info[3] + info[4])/2
        if average >= 90:
            student_grade = 'A'
            student_gpa = 4.0
        elif average >= 80:
            student_grade = 'B'
            student_gpa = 3.5
        elif average >= 70:
            student_grade = 'C'
            student_gpa = 3.0
        elif average >= 60:
            student_grade = 'D'
            student_gpa = 2.0
        else:
            student_grade = 'F'
            student_gpa = 1.0
        self.Error_message.insertPlainText(f"{info[0]} {info[1]}'s grade for this semester is {student_grade}")
        return student_gpa

    def write_csv_file(self):
        row = self.retrieve_information()
        info_list = []
        i = 0
        while i <= 4:
            info_list.append(row[i])
            i += 1
        with open('grade_info.csv', 'a', newline="") as info:
            write_info = writer(info)
            write_info.writerow(info_list)
            info.close()

    def clear(self):
        self.input_first.clear()
        self.input_last.clear()
        self.input_midterm.clear()
        self.input_final.clear()

