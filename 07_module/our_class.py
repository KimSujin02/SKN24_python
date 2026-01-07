import random

teacher_name = '남윤진'
student_count = 29

def study() :
    print(f'{student_count}명의 학생들이 열공중🔥')

def lecture() :
    print(f'{teacher_name} 선생님 수업중!')

def go_lunch(menus) :
    return random.choice(menus)