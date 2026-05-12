import streamlit as st
import google.generativeai as genai

import streamlit as st
    # 頁面初始化設定
st.set_page_config(
page_title="中科 AI 客服 - 闕老師實戰班",
page_icon=" ",
layout="wide" # "wide" 可利用全螢幕寬度,適合放置儀表板
)
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="中科推廣部")
    st.title("系統控制台")
    # 建立下拉選單讓使用者切換服務
    service_type = st.selectbox(
    "請選擇服務類別:",
    ["一般諮詢","技術支援","投訴建議"]
    )
    # 增加 AI 創意度調整桿
    temp = st.slider("AI 靈活度(Temperature)", 0.0, 1.0, 0.7)
    
    st.divider() # 畫出一條美觀的分隔線
    st.info(f"當前連線:{service_type}")

import time
# 使用 st.status 呈現專業的多步驟處理過程
with st.status("AI 正在思考中...", expanded=True) as status:
    st.write("正在讀取 Gemini API Key...")
    time.sleep(1)
    st.write("正在掃描輸入內容安全性...")
    time.sleep(1)
    st.write("正在生成最佳回覆內容...")
    time.sleep(1)
    status.update(label="回覆生成成功!", state="complete", expanded=False)
    
# 或者是使用 st.empty() 進行簡單的原地內容更新
placeholder = st.empty()
placeholder.warning(" 正在思考中...")
time.sleep(2)
placeholder.success(" 回覆完成!")

import streamlit as st
from thefuzz import process

# 建立敏感詞黑名單
BAD_WORDS = ["炸彈", "毒品", "自殺", "暴力"]

# 使用者輸入文字
user_text = st.text_input("請輸入文字進行檢測:")

if user_text:
    # 找出最相似的詞與分數 (0-100)
    match_word, score = process.extractOne(user_text, BAD_WORDS)
    
    st.write(f"系統偵測結果: 相似詞 【{match_word}】(可疑分數: {score})")
    
    if score > 80:
        st.error("偵測到違規訊息，本系統拒絕處理。")
    else:
        st.success("安全檢查通過，正在傳送給 AI 大腦。")
