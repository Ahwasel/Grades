student_name = 'ramy ibrahim'
student_id = '20201000071'

print('Name: ', student_name)
print('ID: ', student_id)

def calculate_grade (mark):
    grade=''
    if mark >= 81:
        grade='excellent'
    elif mark >= 71:
        grade='very good'
    elif mark >=61:
        grade='good'
    elif mark >=51:
        grade='weak'
    elif mark ==50:
        grade='pass'
    else:
        grade='fail'
    return grade 

print('python programming 101: ', calculate_grade(87))
print('math: ', calculate_grade(81))
print('physics: ', calculate_grade(71))
