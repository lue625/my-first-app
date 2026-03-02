import streamlit as st

st.title("未経験パパのアプリ開発：第一歩")
st.write("まずは簡単なBMI計算機を作ってみました。")

# 入力フォーム
weight = st.number_input("体重 (kg)", value=70.0)
height_cm = st.number_input("身長 (cm)", value=170.0)

# 計算ロジック
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

# 結果表示
st.subheader(f"あなたのBMIは {bmi:.2f} です")

if bmi < 18.5:
    st.warning("痩せ気味です。しっかり食べてくださいね！")
elif bmi < 25:
    st.success("標準体型です。キープしましょう！")
else:
    st.error("少し食べすぎかもしれません。ボルダリングに行きましょう！")