import our_class as oc

# our_class 모듈을 가져와서
# 선생님 이름과 학생수를 출력하고
# study()함수와 lecture() 함수를 호출하고
# 먹고 싶은 메뉴명이 5개가 담긴 menus 배열을 만들어서
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!

print('선생님 : ', oc.teacher_name)
print('학생수 : ',oc.student_count)

oc.study()
oc.lecture()

menus = ['구내식당', '컵라면', '든든한거', '맛있는거', '비싼거', '저렴한거']
print(oc.go_lunch(menus))