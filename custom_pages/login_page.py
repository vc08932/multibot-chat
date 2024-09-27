import streamlit as st
from utils.user_manager import user_manager  # 确保这行导入存在

def login_page():
    st.title("登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type='password')
    if st.button("登 录", type='primary', use_container_width=True):
        if user_manager.login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            token = user_manager.generate_token(st.session_state.username)
            redirect_url = f"/?token={token}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={redirect_url}">', unsafe_allow_html=True)
        else:
            st.warning("用户名或密码错误")

    if st.button("注 册", use_container_width=True):
        st.session_state.page = "register_page"
        st.rerun()

