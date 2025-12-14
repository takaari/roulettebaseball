import streamlit as st
import random
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="⚾ 野球ルーレット", layout="centered")
st.title("⚾ 野球ルーレット")

# -------------------------
# セッションステート
# -------------------------
if "angle" not in st.session_state:
    st.session_state.angle = 0

# -------------------------
# 回すボタン
# -------------------------
if st.button("🎯 ルーレットを回す"):
    # ⭐ 角度を「加算」するのがポイント
    st.session_state.angle += random.randint(720, 1440)  # 2〜4回転

# -------------------------
# 画像読み込み
# -------------------------
roulette_b64 = img_to_base64("images/野球ルーレット.png")
umpire_b64 = img_to_base64("images/審判.png")

# -------------------------
# HTML表示
# -------------------------
roulette_html = f"""
<div style="text-align:center;">
  <div style="
    width:300px;
    height:300px;
    margin:auto;
    transition: transform 3s ease-out;
    transform: rotate({st.session_state.angle}deg);
  ">
    <img src="data:image/png;base64,{roulette_b64}" width="300">
  </div>

  <div style="margin-top:20px;">
    <img src="data:image/png;base64,{umpire_b64}" width="120">
  </div>
</div>
"""

st.components.v1.html(roulette_html, height=480)
