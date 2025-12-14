import streamlit as st


st.title("⚾ ルーレットベースボール")

html = """
<style>
#roulette-container {
    text-align: center;
    margin-top: 20px;
}

#roulette {
    width: 380px;
    cursor: pointer;
    transition: transform 3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

#umpire {
    width: 120px;
    margin-top: 20px;
}
</style>

<div id="roulette-container">
    <img id="roulette" src="images/野球ルーレット.png">
    <br>
    <img id="umpire" src="images/審判.png">
</div>

<script>
let angle = 0;
const roulette = document.getElementById("roulette");

roulette.onclick = () => {
    // 3～6回転分ランダム
    const spin = Math.floor(Math.random() * 1080) + 1080;
    angle += spin;
    roulette.style.transform = `rotate(${angle}deg)`;
};
</script>
"""

st.components.v1.html(html, height=600)

