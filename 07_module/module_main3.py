# import-as, from-import 구문
# our_class_pkg의 official 패키지의
# official_module을 별칭 om을 달아 가져오고
# our_class_pkg의 unofficial 패키지의
# unofficial_module을 from-import로 가져와서
# 똑같이 실행
import our_class_pkg.official.official_module as om
from our_class_pkg.unofficial.unofficial_module import study, go_lunch

print('선생님 : ', om.teacher_name)
print('학생수 : ', om.student_count)

study()
om.lecture()

menus = ['구내식당', '컵라면', '든든한거', '맛있는거', '비싼거', '저렴한거']
print(go_lunch(menus))