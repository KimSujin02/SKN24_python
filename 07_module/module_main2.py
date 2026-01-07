# from-import 구문
from our_class import teacher_name, student_count, study, lecture, go_lunch

# our_class 모듈을 가져와서
# 선생님 이름과 학생수를 출력하고
# study()함수와 lecture() 함수를 호출하고
# 먹고 싶은 메뉴명이 5개가 담긴 menus 배열을 만들어서
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!

print('선생님 : ', teacher_name)
print('학생수 : ', student_count)

study()
lecture()

menus = ['구내식당', '컵라면', '든든한거', '맛있는거', '비싼거', '저렴한거']
print(go_lunch(menus))