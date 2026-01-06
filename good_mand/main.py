import time
import random

# DB 연동하기 전 랭킹 리스트
ranking = []

# 마지막에 다 보여주기!
user_info = {
    "name" : ""
    , "total_score" : 0
    , "step_1_score" : 0 # 재료 점수
    , "step_2_score" : 0 # 양념 점수
    , "step_3_score" : 0 # 다지기 점수
    , "step_4_score" : 0 # 찜기 점수
}

# 1단계 재료 리스트 (정답 리스트 총 50)
# best 점수 : 30
# good 점수 : 20 ~ 24
# not_good 점수 : 19점 이하
ingredient_list = [
    {"name": "돼지고기(앞다리)", "score": 10},
    {"name": "돼지고기(뒷다리)", "score": 5},
    {"name": "양배추", "score": 5},
    {"name": "부추", "score": 5},
    {"name": "양파", "score": 5},
    {"name": "두부", "score": 5},
    {"name": "당면", "score": 5},
    {"name": "대파", "score": 5},
    {"name": "쑥", "score": -5},
    {"name": "미나리", "score": -5},
    {"name": "마늘쫑", "score": -5},
    {"name": "다진 김치", "score": -15},
    {"name": "묵은 김치", "score": -15},
    {"name": "겉절이 김치", "score": -15},
    {"name": "베이컨", "score": -15},
    {"name": "소시지", "score": -15},
    {"name": "깻잎", "score": -15},
    {"name": "샐러리", "score": -15},
    {"name": "브로콜리", "score": -15}
]

# 2단계 양념 재료 리스트 (정답 리스트 총 40)
# best 점수 : 25
# good 점수 : 20 ~ 24
# not_good 점수 : 19점 이하
seasoning_list = [
    {"name": "다진 마늘", "score": 5},
    {"name": "간장", "score": 5},
    {"name": "참기름", "score": 5},
    {"name": "후추", "score": 5},
    {"name": "소금", "score": 5},
    {"name": "설탕", "score": 5},
    {"name": "슬라이스 치즈", "score": -5},
    {"name": "크림치즈", "score": -5},
    {"name": "버터", "score": -5},
    {"name": "마요네즈", "score": -5},
    {"name": "라면 스프", "score": -5},
    {"name": "떡볶이", "score": -5},
    {"name": "식빵", "score": -5},
    {"name": "사과", "score": -5}
]

judge_list = [
    "만두 장인 [백두산]",
    "전통요리연구가 [명지광]",
    "미각명인 [좌청룡]",
    "만두대법관 [엄덕구]",
    "찜기의 수호자 [탁귀핑]",
    "속재료 감정관 [왕대협]",
    "국물의 신 [사마귀]",
    "만두왕국 대심사관 [팔광구]"
]

judge_face1 = """
              ┌─────────────┐
              │   ಠ     ಠ   │
              │      _      │
              │    ────     │
              └─────────────┘
    """

judge_face2 = """
              ┌─────────────┐
              │   ಠ     ಠ   │
              │      _      │
              │    ╱~~~╲    │
              └─────────────┘
    """

judge_face3 = """
              ┌─────────────┐
              │   ಠ     ಠ   │
              │     ╱╲     │
              │    ╱0╲     │
              └─────||─────┘
                    ││
                    ││
                    ╱╱
"""

# 키보드로 다지기 점수
# best : 200자
# 	점수 : 100
# good : 150자 ~ 199자
# 	점수 : 50
# not_good : 149자 이하
# 	점수 : 10

# 게임 끝나면 user_list 초기화 하는 메서드
def game_done() :
    ranking.append(user_info)
    user_info = {
        "name" : ""
        , "total_score" : 0
        , "step_1_score" : 0 # 재료 점수
        , "step_2_score" : 0 # 양념 점수
        , "step_3_score" : 0 # 다지기 점수
        , "step_4_score" : 0 # 찜기 점수
    }

# 게임 끝나면 랭킹 리스트 정렬해서 보여줌!
def show_ranking() :
    print("""
          🥟🥟🥟🥟🥟 만 두 게 임 랭 킹 🥟🥟🥟🥟🥟
          """)
    ranking.sort(key=lambda x: x["total_score"], reverse=True)
    for i, user in enumerate(ranking[:5]):
        print(f"{i+1}등 : {user['name']} ({user['total_score']}점)")
    
    input("다시 시작하려면 엔터를 눌러주세요!")

# 최종 점수 구하기!
def get_total_score() :
    user_info['total_score'] += user_info['step_1_score']
    user_info['total_score'] += user_info['step_2_score']
    user_info['total_score'] += user_info['step_3_score']
    user_info['total_score'] += user_info['step_4_score']

def judge_mandu() :
    get_total_score()
    time.sleep(1)
    print(judge_face1)
    print(f'안녕하세요 심사위원 {random.choice(judge_list)}입니다.')
    print("...")
    time.sleep(1)
    print(f'총 점수는 {user_info['total_score']}입니다.')
    
    # 150
    # 100 ~ 149
    if user_info['total_score'] >= 150 :
        print(judge_face1)
        print("맛있네요.")
    elif 100 <= user_info['total_score'] <= 149 :
        print(judge_face2)
        print("으 토가 나올 것만 같군요")
    else :
        print(judge_face3)
        print("제 인생 최악의 만두입니다. 으어어어어얽.")
        
        
    

def choice_step_1() :
    print('1단계!\n기본 재료를 5가지 선택해주세요!🥗')
    random.shuffle(ingredient_list)
    for idx, obj in enumerate(ingredient_list) :
        if idx % 5 == 0 :
            print()
        print(obj['name'], end='  ')
    print()
    ingredient_score = 0
    selected_ingredient = []
    
    ingredient_names = [item["name"] for item in ingredient_list]
    for n in range(0, 5) :
        print(f'{n+1}번째 재료를 입력해주세요!')
        while True:
            temp = str(input('입력 : '))
            if temp in selected_ingredient :
                print('이미 선택한 재료입니다! 다시 입력해주세요.')
                print(f'현재 선택한 재료 리스트 : {selected_ingredient}')
                continue
            elif not (temp in ingredient_names):
                print('재료 리스트에 존재하지 않는 값입니다!!')
                continue
            else :
                for item in ingredient_list:
                    if item["name"] == temp:
                        ingredient_score += item["score"]
                selected_ingredient.append(temp)
                break
    time.sleep(1)
    print('⭐⭐⭐재료 선택이 완료 되었어요!⭐⭐⭐')
    time.sleep(1)
    print(selected_ingredient)
    user_info['step_1_score'] = ingredient_score
    ingredient_score_calc()
        
def ingredient_score_calc() :
    score = user_info['step_1_score']
    eval = ""
    print(f'재료 점수는 : {score}점 입니다!')
    time.sleep(1)
    if score >=30 :
        eval = "최고!! 🥰🥰🥰"
    elif 25 <= score <= 29 :
        eval ="굿 😋"
    else :
        eval ='최악!!!!!!!!!! 🤮🤮🤮🤮🤮🤮'
    print(f'평가(최고/굿/최악) : {eval}')
    
    input("이제 만두를 찌러 가볼까요? (엔터를 눌러주세요!)")
    

def random_bonus_score() :
    score = random.randint(-30, 100)
    return score

def steamer() :
    messages = [
    """
            ______________________
         .-''                      ''-.
       .'        o      o      o         '.
      /        o      o      o      o       \\
     |      o        o      O      o          |
     |            o        o      o           |
      \\                                      /
       '.                                  .'
         '-.____________________________.-'

        |                                  |
        |                                  |
        |                                  |
        |                                  |
        |                                  |
        |__________________________________|
          🔥   🔥   🔥   🔥   🔥   🔥
           🔥   🔥   🔥   🔥   🔥
    """,
    """
        🔥   🔥   🔥  보글 🔥   🔥   🔥
        🔥   🔥   🔥   🔥   🔥
    """ ,
    """
                    🔥   🔥   🔥   🔥   🔥   🔥
                    🔥   🔥   🔥보글   🔥   🔥
    """,
    """
            🔥   🔥   🔥   🔥   🔥   🔥
            🔥   🔥   보글🔥   🔥   🔥
    """
    ]

    for msg in messages:
        print(msg)
        time.sleep(0.5)
    
    steamer_score = random_bonus_score()
    if steamer_score < 0 :
        print(f'으악 만두를 찌다가 문제가 생겼어요.. 😭 : {steamer_score}점')
    else :
        print(f'찜이 잘 돼서 보너스 포인트를 받았어요! : +{steamer_score}점')
    time.sleep(1)
    print('만두 완성!! 이제 심사위원한테 평가를 받아볼게요.')

def game_start() :
    # 게임 시작하면 먼저 user name 받기
    user_info['name'] = str(input('안녕하세요! 만두게임 도전자 이름을 입력해주세요! :'))
    choice_step_1()
    steamer()
    judge_mandu()
    
game_start()