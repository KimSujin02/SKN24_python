import streamlit as st

st.title('사용자 입력 받는 페이지✏️')

# 컬럼 란을 3개 만들라는 ui 설정
# _는 그냥 비워 놓는 거 같음
col1, _, col2 = st.columns(3)

with col1 :
    nickname = st.text_input('닉네임 입력')
    age = st.number_input('나이 입력', min_value=13, max_value=100)
    
    national_option = ['대한민국','일본','중국','미국', '프랑스', '영국']
    national = st.selectbox('국적', national_option)
    
    hobby_option = ['게임', '독서', '유튜브', '뜨개', '음악감상']
    hobby = st.radio('취미', hobby_option)
    
    is_checked = st.checkbox('개인정보 제공 동의')
with col2 :
    st.badge('결과보기!')
    if st.button('✅ 입력 완료') :
        st.write(f'이름이 뭐야? {nickname}')
        st.write(f'몇 살이야? {age}')
        st.write(f'국적이 뭐야? {national}')
        st.write(f'취미가 뭐야? {hobby}')
        st.write(f'개인정보 제공 동의함? {is_checked}')