import streamlit as st # 외부 라이브러리를 사용하다보면 별칭이 존재함
import good_mandu.art as art
import good_mandu.main as mandu
import random
import time

st.set_page_config(
    page_title="🥟🥟굿 만두, 그레이트 만두🥟🥟",
    page_icon="🥟"
)

st.title('🥟🥟굿 만두, 그레이트 만두🥟🥟')

mandu.mode = 'e'

if "step" not in st.session_state:
    st.session_state.step = 1

text_area = st.empty()
select_area = st.empty()
button_area = st.empty()
warning_area = st.empty()

mandu.user_info['name'] = text_area.text_input('안녕하세요! 만두게임 도전자 이름을 입력해주세요!')

if mandu.user_info['name'] :
    if st.session_state.step == 1 :
        st.text(f'1단계!\n재료를 5가지 선택해주세요!🥗')
        
        if "choice_list" not in st.session_state :
            st.session_state.choice_list = mandu.ingredient_list
            random.shuffle(st.session_state.choice_list)
        
        st.session_state.selected_list = []
        
        choice_names = [item["name"] for item in st.session_state.choice_list]
        choice_score = 0
        
        cols = st.columns(5)
        for idx, item in enumerate(choice_names) :
            with cols[idx % 5]:
                if st.checkbox(item, key=f"chk_{item}"):
                    st.session_state.selected_list.append(item)
        button_area = st.empty()
        if st.button("재료 선택 완료!"):
            if len(st.session_state.selected_list) == 5:
                st.session_state.step = 2
            else :
                warning_area.warning('5가지를 선택해주세요!')
    if st.session_state.step >= 2:
        choice_score = 0
        for item in st.session_state.choice_list:
            for temp in st.session_state.selected_list:
                if item["name"] == temp:
                    choice_score += item["score"]

        mandu.user_info['step_1_score'] = choice_score

        if choice_score >= 40:
            eval = "최고!! 🥰🥰🥰"
        elif 20 <= choice_score <= 39:
            eval = "굿 😋"
        else:
            eval = "최악!!!!!!!!!! 🤮🤮🤮🤮🤮🤮"
        
        text = f"""
        ⭐⭐⭐1단계 재료 평가⭐⭐⭐
        재료 점수: {choice_score}점
        평가: {eval}
        {art.ready_to_steam}
        """
        text_area.text(text)

        if button_area.button("이제 만두를 완성하러 가볼까요? 😋"):
            st.session_state.step = 3
    if st.session_state.step == 3 :
        msg = st.empty()
        msg.info("만두 찌는 중... 🥟 (조금만 기다려주세요!)")
        
        pot = st.empty()
        
        messages = [
            '보글보글...'
            , '...보글보글...'
            , '보글보글...'
            , '...보글보글...'
        ]
        
        for m in messages:
            pot.text(m)
            time.sleep(0.5)
        
        steamer_score = random.randint(-30, 100)
        if steamer_score < 0 :
            st.text(f'으악 만두를 찌다가 문제가 생겼어요.. 😭 : {steamer_score}점')
        else :
            st.text(f'찜이 잘 돼서 보너스 포인트를 받았어요! 🥰 : +{steamer_score}점')
        
        mandu.user_info['total_score'] += steamer_score
        if st.button("만두 완성!! 이제 심사위원한테 평가를 받아볼게요."):
            st.session_state.step = 4
    if st.session_state.step == 4 :
        mandu.get_total_score()
        judge_face_area = st.empty()
        judge_face_area.text(art.judge_face1)
        judge_area = st.empty()
        judge_area.info(f'안녕하세요 심사위원 {random.choice(mandu.judge_list)}입니다.')
        time.sleep(2)
        judge_area.info('흠.. 오호.. 그렇구나...')
        time.sleep(2)
        judge_area.info(f'총 점수는 {mandu.user_info['total_score']}입니다.')
        if mandu.user_info['total_score'] >= 80 :
            judge_face_area.text(art.judge_face4)
            judge_area.info('?!')
            time.sleep(2)
            judge_area.info('우오오!!!')
            time.sleep(2)
            judge_area.info('너무 맛있습니다!!!❤️❤️❤️❤️❤️❤️❤️❤️❤️')
        elif 50 <= mandu.user_info['total_score'] <= 79 :
            judge_face_area.text(art.judge_face2)
            judge_area.info("으.. 토가 나올것만 같군요")
        else :
            judge_face_area.text(art.judge_face3)
            judge_area.info("제 인생 최악의 만두입니다. 으어어어어얽.")