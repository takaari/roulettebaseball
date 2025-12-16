import streamlit as st
import base64
import random

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="⚾ 野球ルーレット", layout="centered")
st.title("⚾ 野球ルーレット")

roulette_b64 = img_to_base64("images/野球ルーレット.png")
umpire_b64 = img_to_base64("images/審判.png")

spin = st.button("🎯 ルーレットを回す")

html = f"""
<div style="text-align:center;">
  <div id="wheel" style="
    width:300px;
    height:300px;
    margin:auto;
    transition: transform 3s ease-out;
  ">
    <img src="data:image/png;base64,{roulette_b64}" width="300">
  </div>

  <div style="margin-top:20px;">
    <img src="data:image/png;base64,{umpire_b64}" width="120">
  </div>
</div>

<script>
let angle = 0;

function spinWheel() {{
  const wheel = document.getElementById("wheel");
  angle += Math.floor(Math.random() * 720) + 720;
  wheel.style.transform = `rotate(${{angle}}deg)`;
}}

{"spinWheel();" if spin else ""}
</script>
"""

st.components.v1.html(html, height=480)
