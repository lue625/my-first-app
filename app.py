import streamlit as st
import base64
import os

# 1. ページ設定
st.set_page_config(page_title="クライマー・パパの記録", page_icon="🧗‍♂️", layout="centered")

# 2. ローカル画像を背景に設定する関数
def set_bg_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            .stApp::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.4); /* 背景の透かし具合を調整 */
                z-index: -1;
            }}
            .stCard {{
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                margin-bottom: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        # 画像がない場合の予備設定（単色背景など）
        st.warning("背景画像 (bg.jpg) が見つかりません。GitHubにアップロードしてください。")

# 背景の設定実行（ファイル名を指定）
set_bg_local("bg.jpg")

# --- メインコンテンツ ---

st.title("🧗‍♂️ クライマーの成長記録")
st.write("家族のために健康を維持し、最高グレードを目指しましょう！")

# 【最高グレード記録】
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.subheader("🏆 最高グレード")

grades = ["10級", "9級", "8級", "7級", "6級", "5級", "4級", "3級", "2級", "1級", "初段", "二段", "三段"]
col1, col2 = st.columns([2, 1])
with col1:
    current_max_grade = st.selectbox("現在の最高グレードは？", grades, index=4)
with col2:
    if st.button("記録を更新！"):
        st.balloons()
        st.success(f"おめでとう！ {current_max_grade} に更新！")
st.markdown("</div>", unsafe_allow_html=True)

# 【健康状態チェッカー】
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.subheader("⚖️ 健康状態 (BMI)")

col3, col4 = st.columns(2)
with col3:
    weight = st.number_input("体重 (kg)", value=70.0, step=0.1)
with col4:
    height_cm = st.number_input("身長 (cm)", value=170.0, step=0.1)

height_m = height_cm / 100
bmi = weight / (height_m ** 2)
st.write(f"現在のBMIは **{bmi:.2f}** です。")

if bmi < 25:
    st.success("標準体型です！その調子！")
else:
    st.error("少し体が重いかも？食事管理を意識しましょう。")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("。")