import random
import our_class_pkg.official.official_module as om

def study() :
    print(f'{om.student_count}명의 학생들이 열공중🔥')

def go_lunch(menus) :
    return random.choice(menus)