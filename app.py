import streamlit as st
import pandas as pd
import numpy as np
from result import mbti
import time


# Initialization
if 'vector' not in st.session_state:
    st.session_state['vector'] = np.array([0,0,0,0,0,0,0,0])
if 'progress' not in st.session_state:
    st.session_state['progress'] = np.array([0.0])
    # 데이터 벡터초기화
if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_csv('data.csv')
    df = st.session_state['df']
    df['vector'] = df.apply(lambda x: np.array([x[i] for i in range(2,10)]),axis=1)
    # 위치는 고정할것
    # df = df.sample(frac=1).reset_index(drop=True)
    # st.session_state['df'] = df
    # print(df)
if 'idx' not in st.session_state:
    st.session_state['idx'] = np.array([0])

progress = st.session_state['progress']
now_vector = st.session_state['vector']
idx = st.session_state['idx']
df = st.session_state['df']

if progress[0]<=1:
    progress[0] +=1/12
else:
    progress[0] =1


#==============================================================================
st.markdown("<h1 style='text-align: center;'>그림으로 알아보는</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>내 MBTI는? </h2>", unsafe_allow_html=True)

st.markdown("-----")


if idx[0]<(len(df)):
    st.markdown("<h3 style='text-align: center;'> 마음에 드는 사진을 고르세요 </h3>", unsafe_allow_html=True)
        
    #=============================================row1
    url_1 = df['url'].iloc[idx[0]]
    url_1_vector = df['vector'].iloc[idx[0]]

    url_2 = df['url'].iloc[idx[0]+1]
    url_2_vector = df['vector'].iloc[idx[0]+1]


    #=============================================row2
    def click_1():
        global now_vector
        global idx
        now_vector +=url_1_vector
        idx[0] +=2
        return now_vector,idx
    def click_2():
        global now_vector
        global idx
        now_vector +=url_2_vector
        idx[0] +=2
        return now_vector,idx
        
    #=============================================row2


    col1, col2 = st.columns(2)
    with col1:
        result_img1 = st.image(url_1)
        col1.button('1번',on_click = click_1)
    with col2:
        result_img2 = st.image(url_2)
        col2.button('2번',on_click = click_2)

    st.markdown(f"<h3 style='text-align: center;'> 진행률{int(idx[0]/2)+1}/12 </h3>", unsafe_allow_html=True)
    st.progress(progress[0])
    
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.info("이미지는 AI로 생성된 이미지입니다.")
    
    
    
else:
    st.markdown("<h3 style='text-align: center;'> 결과를 확인하세요 </h3>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    col1,col2,col3 = st.columns(3)
    with col2:
        if col2.button("결과확인"):
            with st.spinner('잠시만 기다려 주세요!'):
                time.sleep(5)
       
                st.markdown("<h3 style='text-align: center;'> 당신의 MBTI는 </h3>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='text-align: center;'> {mbti(now_vector)} </h2>", unsafe_allow_html=True)
