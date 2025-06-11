import streamlit as st

positions = {
    "골키퍼 🧤": {
        "역할": "골문을 지키며 상대 팀의 슈팅을 막는 최후의 수비수입니다.",
        "중요성": "팀의 마지막 방어선으로, 승패에 큰 영향을 끼칩니다! 🛡️"
    },
    "수비수 🛡️": {
        "역할": "상대 공격수를 막고, 공을 빼앗아 팀의 골문을 지킵니다.",
        "중요성": "팀의 안정성을 책임지는 핵심 포지션입니다! 💪"
    },
    "미드필더 🎯": {
        "역할": "공격과 수비를 연결하며 경기를 조율하는 플레이메이커입니다.",
        "중요성": "팀의 심장으로서 경기를 지배합니다! ❤️‍🔥"
    },
    "공격수 ⚡️": {
        "역할": "골을 넣기 위해 상대 골문을 적극적으로 공격합니다.",
        "중요성": "팀 승리의 희망! 결정적인 순간을 만들어내는 스타입니다! 🌟"
    },
    "윙어 🌪️": {
        "역할": "측면에서 빠른 돌파와 크로스를 담당합니다.",
        "중요성": "공격의 활력을 불어넣는 에너지맨! 🔥"
    }
}

st.markdown("""
<style>
    .title {
        font-size: 48px;
        font-weight: 900;
        color: #1e90ff;
        text-align: center;
        text-shadow: 3px 3px 8px #00bfff;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 28px;
        color: #ff6347;
        margin-top: 30px;
        font-weight: bold;
    }
    .content {
        font-size: 20px;
        color: #333333;
        background: #f0f8ff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(30,144,255,0.4);
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #999999;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">⚽ 축구 포지션 안내 🌟</div>', unsafe_allow_html=True)

selected_position = st.selectbox("👇 포지션을 선택하세요!", list(positions.keys()))

st.markdown(f'<div class="section-title">📌 역할</div>', unsafe_allow_html=True)
st.markdown(f'<div class="content">{positions[selected_position]["역할"]}</div>', unsafe_allow_html=True)

st.markdown(f'<div class="section-title">🔥 중요성</div>', unsafe_allow_html=True)
st.markdown(f'<div class="content">{positions[selected_position]["중요성"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ⚽ and ❤️ by ChatGPT</div>', unsafe_allow_html=True)
