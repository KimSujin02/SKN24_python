import streamlit as st

st.title('Counter')

# 그냥 일반 문법으로 변수를 만들고 초기화하면
# 요소가 변경되면서(클릭) 코드의 첫줄부터 시작돼서 count가 늘어나지 않음
# 세션에 customer_counter가 없는 경우 세션에 customer_counter 다시 생성
# 세션에 customer_counter가 있는 경우, 진행되지 않음
if "customer_counter" not in st.session_state :
    st.session_state.customer_counter = 0

if st.button("손님 들어오십니다!") :
    st.session_state.customer_counter += 1
    st.write(f'오늘의 손님 수 : {st.session_state.customer_counter}')

if st.button("오늘 장사 끝! 손님 수 초기화!") :
    st.session_state.customer_counter = 0
    st.write(f'오늘의 손님 수 : {st.session_state.customer_counter}')