import csv
from csv import *
from PyQt6.QtWidgets import *
from GPA import *

class Logic (QMainWindow, Ui_MainWindow):
    gpa_list = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        file_name = 'grade_info.csv'
        f = open(file_name, 'w+')
        f.close()
        self.GPA_display.clear()
        self.submit_student_buttom.clicked.connect(lambda: self.student_submit())
        self.submit_final_button.clicked.connect(lambda: self.final_submit())

# submitting the student information
# count number of students as student information is submitted
    def student_submit(self):
        self.retrieve_information()
        self.write_csv_file(self.retrieve_information())  # input student information
        self.determine_grade(self.retrieve_information())  # determine the grade letter
        self.student_clear()  # clear student information input


# final submission/ display the GPA for each student
    def final_submit(self):
        self.final_message.insertPlainText(f"Please check the csv file for the student's "
                                           f"first name, last name, school year, midterm score, "
                                           f"and final exam score.")
        self.gpa_display(self.gpa_list)
        self.student_clear()

# retrieve student information from input \
# create a list of retrieved information(fist,last,school year,midterm,final,average)
# append average score to a separate list
    def retrieve_information(self):
        try:
            first_name = str((self.input_first.text()).strip().upper())
            last_name = str((self.input_last.text()).strip().upper())
            if self.freshman.isChecked():
                school_year = 'Freshman'
            elif self.sophomore.isChecked():
                school_year = 'Sophomore'
            elif self.junior.isChecked():
                school_year = 'Junior'
            else:
                school_year = 'Senior'
            midterm = int((self.input_midterm.text()).strip())
            final = int((self.input_final.text()).strip())
            row = [first_name, last_name, school_year, midterm, final]
            return row
        except:
            self.Error_message.clear()
            self.Error_message.insertPlainText(f'Please input the correct information.')
            row = []
            return row

# determine the GPA and grade in letter
    def determine_grade(self,information):
        if len(list(information)) == 0:
            self.Error_message.clear()
            self.Error_message.insertPlainText(f'Please input the correct information.')
            return False
        else:
            info_list = list(information)
            average = (info_list[3] + info_list[4])/2
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
            self.gpa_list.append(student_gpa)
            self.Error_message.clear()
            self.Error_message.insertPlainText(f"{info_list[0]} {info_list[1]}'s average score is {average:.2f} "
                                               f"and the grade for this semester is {student_grade}.")
            return self.gpa_list

    def write_csv_file(self, information):
        if len(list(information)) == 0:
            return False
        else:
            info_list = list(information)
            with open('grade_info.csv', 'a', newline="") as info:
                write_info = writer(info)
                write_info.writerow(info_list)
                info.close()
            return 'grade_info.csv'

    def gpa_display(self, gpa_list):
        student_gpa = list(gpa_list)
        i = 0
        with open('grade_info.csv') as file_object:
            reader_object = csv.reader(file_object)
            while i < len(student_gpa):
                for row in reader_object:
                    self.GPA_display.insertPlainText(f"{row[0]} {row[1]}'s GPA is {student_gpa[i]}.\n")
                    i += 1

    def student_clear(self): # clear individual student information
        self.input_first.clear()
        self.input_last.clear()
        self.input_midterm.clear()
        self.input_final.clear()



