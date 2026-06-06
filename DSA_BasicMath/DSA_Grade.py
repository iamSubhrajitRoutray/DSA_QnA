''' Q) Mapping score of the student'''

class grading:
    
    def student_grade(self, marks):
    
        if marks >= 90:

            print('Grade A')
    
        elif marks >= 70:

            print('Grade B')
    
        elif marks >= 50:

            print('Grade C')
    
        elif marks >= 35:

            print('Grade D')
    
        else:

            print('Fail')


# Main/Driver code : 
obj = grading()

obj.student_grade(80)

