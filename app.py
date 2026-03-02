import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="クライマー・パパの記録", page_icon="🧗‍♂️", layout="centered")

# 2. 背景画像とカスタムCSS（ここを修正しました）
bg_img_url = "https://images.unsplash.com/photo-1516109968846-559d18e3c153?q=80&w=1920&auto=format&fit=crop"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_img_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.6);
        z-index: -1;
    }}
    .stCard {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }}
    h1, h2, h3 {{
        color: #2c3e50;
    }}
    </style>
    """,
    unsafe_allow_html=True  # ← ここを1つだけに修正しました
)

# --- ここからメインコンテンツ ---

st.title("🧗‍♂️ クライマー・パパの成長記録")
st.write("家族のために健康を維持し、最高グレードを目指しましょう！")

# 【最高グレード記録】セクション
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.subheader("🏆 最高グレード")

grades = [
    "10級", "9級", "8級", "7級", "6級", "5級", "4級", "3級", "2級", "1級",
    "初段", "二段", "三段", "四段"
]

col1, col2 = st.columns([2, 1])
with col1:
    current_max_grade = st.selectbox("あなたの現在の最高グレードは？", grades, index=4)
with col2:
    if st.button("記録を更新！"):
        st.balloons()
        st.success(f"{current_max_grade} に更新しました！")

st.markdown("</div>", unsafe_allow_html=True)

# 【健康状態チェッカー】セクション
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.subheader("⚖️ 健康状態 (BMI)")

col3, col4, col5 = st.columns(3)
with col3:
    weight = st.number_input("体重 (kg)", value=70.0, step=0.1)
with col4:
    height_cm = st.number_input("身長 (cm)", value=170.0, step=0.1)
with col5:
    target_weight = st.number_input("目標体重 (kg)", value=65.0, step=0.1)

height_m = height_cm / 100
bmi = weight / (height_m ** 2)
diff = weight - target_weight

st.write(f"現在のBMIは **{bmi:.2f}** です。")

if bmi < 18.5:
    st.warning("痩せ気味です。保持力アップのために、もう少し食べましょう！")
elif bmi < 25:
    st.success("標準体型です。クライミングに理想的！")
else:
    st.error("肥満気味です。体が重いと関節への負担が大きくなります。")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("未経験パパがアプリ開発で脱サラを目指す物語。応援よろしくお願いします！")