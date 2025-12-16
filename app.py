import streamlit as st
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="⚾ 野球ルーレット", layout="centered")
st.title("⚾ 野球ルーレット")

roulette_b64 = img_to_base64("images/野球ルーレット.png")
umpire_b64 = img_to_base64("images/審判.png")

html = f"""
<div style="text-align:center; position:relative; width:300px; margin:auto;">

  <!-- ルーレット -->
  <div id="wheel"
       style="
         width:300px;
         height:300px;
         transition: transform 3s ease-out;
         transform: rotate({angle}deg);
       ">
    <img src="data:image/png;base64,{roulette_b64}" width="300">
  </div>

  <!-- 審判（必ず上に表示） -->
  <img src="data:image/png;base64,{umpire_b64}"
       width="120"
       style="
         position:absolute;
         top: 260px;
         left: 50%;
         transform: translateX(-50%);
         z-index: 10;
       ">

</div>



"""

st.components.v1.html(html, height=520)
