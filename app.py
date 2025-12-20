import streamlit as st
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="⚾ 野球ルーレット", layout="centered")
st.title("⚾ 野球ルーレット")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #9f4a23;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


roulette_b64 = img_to_base64("images/野球ルーレット.png")
umpire_b64 = img_to_base64("images/審判.png")

html = f"""
<div style="text-align:center;">
  
  <div id="wheel" style="
    width:300px;
    height:300px;
    margin:auto;
    transition: transform 3s cubic-bezier(.17,.67,.36,1);
  ">
    <img src="data:image/png;base64,{roulette_b64}" width="300">
  </div>

  <div style="margin-top:-10px;">
    <img src="data:image/png;base64,{umpire_b64}" width="120">
  </div>

  <button onclick="spinWheel()" style="
    margin-top:20px;
    font-size:18px;
    padding:8px 20px;
    cursor:pointer;
  ">
    🎯 ルーレットを回す
  </button>
</div>

<script>
let angle = 0;

function spinWheel() {{
  angle += Math.floor(Math.random() * 720) + 720;
  document.getElementById("wheel").style.transform =
    `rotate(${{angle}}deg)`;
}}
</script>
"""

st.components.v1.html(html, height=520)
