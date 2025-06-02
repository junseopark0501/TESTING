import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🔮 나의 ✨환상적인✨ 진로를 찾아볼까요?",
    page_icon="✨",
    layout="wide" # 넓은 레이아웃 사용
)

# --- CSS 스타일링 (더 많은 스타일을 추가할 수 있습니다!) ---
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6; /* 연한 배경색 */
        background-image: linear-gradient(to right, #a1c4fd, #c2e9fb); /* 예쁜 그라데이션 */
    }
    .stSelectbox > div > div > div {
        background-color: #ffffff; /* 드롭다운 배경 흰색 */
        border-radius: 15px;
        border: 2px solid #6a0572;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        padding: 10px;
    }
    .stButton > button {
        background-image: linear-gradient(to right, #ff7e5f, #feb47b); /* 그라데이션 버튼 */
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        padding: 15px 30px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 7px 7px 20px rgba(0,0,0,0.3);
    }
    h1 {
        color: #6a0572; /* 보라색 제목 */
        text-align: center;
        font-size: 3.5em;
        text-shadow: 3px 3px #f7c32b; /* 그림자 효과 */
    }
    h2 {
        color: #e63946; /* 빨간색 부제목 */
        text-align: center;
        font-size: 2.5em;
    }
    h3 {
        color: #2a9d8f; /* 청록색 소제목 */
        font-size: 2em;
    }
    .stExpander {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.05);
    }
    .stExpander > div > div {
        color: #457b9d; /* 익스팬더 내부 텍스트 색상 */
    }
</style>
""", unsafe_allow_html=True)

# --- MBTI 데이터 (이모지와 함께) ---
mbti_data = {
    "ISTJ 🧐": {
        "emoji": "🧐",
        "description": "세상의 소금형, 현실적이고 책임감이 강해요.",
        "jobs": [
            {"name": "회계사 📊", "reason": "정확하고 체계적인 업무에 강해요.", "tasks": "재무 기록 관리, 세금 보고", "skills": "수학, 꼼꼼함"},
            {"name": "공무원 🏛️", "reason": "규칙을 준수하고 안정적인 환경을 선호해요.", "tasks": "행정 업무, 민원 처리", "skills": "정확성, 책임감"},
            {"name": "프로그래머 💻", "reason": "논리적이고 문제 해결에 능숙해요.", "tasks": "소프트웨어 개발, 시스템 관리", "skills": "논리적 사고, 코딩"}
        ]
    },
    "ENFP 🤩": {
        "emoji": "🤩",
        "description": "활동가형, 열정적이고 창의적이며 사회성이 좋아요.",
        "jobs": [
            {"name": "마케터 🗣️", "reason": "창의적인 아이디어와 뛰어난 소통 능력이 강점이에요.", "tasks": "캠페인 기획, 고객 소통", "skills": "창의성, 커뮤니케이션"},
            {"name": "강사/교육자 👩‍🏫", "reason": "새로운 것을 배우고 가르치는 것을 즐겨요.", "tasks": "강의 진행, 교육 콘텐츠 개발", "skills": "열정, 설명 능력"},
            {"name": "작가 ✍️", "reason": "자유로운 사고와 표현에 능숙해요.", "tasks": "글쓰기, 스토리텔링", "skills": "상상력, 문장력"}
        ]
    },
    "INTJ 🧠": {
        "emoji": "🧠",
        "description": "전략가형, 분석적이고 독립적이며 통찰력이 뛰어나요.",
        "jobs": [
            {"name": "데이터 과학자 📊", "reason": "복잡한 문제를 분석하고 해결하는 것을 좋아해요.", "tasks": "데이터 분석, 모델링", "skills": "통계, 프로그래밍"},
            {"name": "컨설턴트 📈", "reason": "논리적인 사고로 문제를 진단하고 해결책을 제시해요.", "tasks": "기업 전략 수립, 문제 해결", "skills": "분석력, 문제 해결"},
            {"name": "연구원 🧪", "reason": "지식을 탐구하고 새로운 이론을 정립하는 것에 흥미를 느껴요.", "tasks": "실험, 논문 작성", "skills": "탐구심, 비판적 사고"}
        ]
    },
    "ESFP 🥳": {
        "emoji": "🥳",
        "description": "연예인형, 사교적이고 즉흥적이며 에너지가 넘쳐요.",
        "jobs": [
            {"name": "이벤트 플래너 🎉", "reason": "사람들과 어울리고 즐거운 분위기를 만드는 데 능숙해요.", "tasks": "행사 기획, 진행", "skills": "기획력, 사교성"},
            {"name": "승무원 ✈️", "reason": "활동적이고 새로운 사람들과 만나는 것을 즐겨요.", "tasks": "고객 서비스, 안전 관리", "skills": "친화력, 서비스 정신"},
            {"name": "공연 예술가 🎭", "reason": "자신을 표현하고 사람들에게 즐거움을 주는 것을 좋아해요.", "tasks": "연기, 노래, 춤", "skills": "표현력, 무대 장악력"}
        ]
    }
    # 여기에 더 많은 MBTI 유형과 직업 데이터를 추가하세요!
}

# --- 메인 페이지 ---
st.title("🔮 나의 ✨환상적인✨ 진로를 찾아볼까요? 🔮")
st.markdown("<h2 style='text-align: center;'>MBTI로 알아보는 💫나에게 딱 맞는 직업 추천!💫</h2>", unsafe_allow_html=True)
st.markdown("---") # 구분선

st.write(" ") # 공백
st.markdown("<p style='text-align: center; font-size: 1.2em;'>👋 궁금한 MBTI를 선택하고 나에게 맞는 직업을 탐색해보세요! 🕵️‍♀️</p>", unsafe_allow_html=True)
st.write(" ") # 공백

col1, col2, col3 = st.columns([1,2,1]) # 가운데 정렬을 위한 컬럼 분할

with col2:
    selected_mbti_raw = st.selectbox(
        "✨ 당신의 MBTI는 무엇인가요? ✨",
        list(mbti_data.keys()),
        index=0,
        help="나의 성격을 잘 나타내는 MBTI를 선택해주세요!"
    )

st.write(" ") # 공백

if st.button("🚀 진로 탐험 시작! 🚀"):
    # MBTI 이름만 추출 (이모지 제거)
    selected_mbti_name = selected_mbti_raw.split(" ")[0]

    st.markdown("---") # 구분선
    st.markdown(f"<h1 style='color: #4CAF50; text-align: center;'>✨ 당신은 **{selected_mbti_name}** 이시군요! {mbti_data[selected_mbti_raw]['emoji']} ✨</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.3em;'><i>{mbti_data[selected_mbti_raw]['description']}</i></p>", unsafe_allow_html=True)
    st.write(" ")

    st.markdown(f"<h3>💡 {selected_mbti_name} 유형에게 어울리는 직업 분야는 다음과 같아요! 💡</h3>", unsafe_allow_html=True)

    jobs = mbti_data[selected_mbti_raw]["jobs"]
    for job in jobs:
        with st.expander(f"✨ **{job['name']}**"):
            st.markdown(f"**🎯 이 직업이 {selected_mbti_name} 에게 딱 맞는 이유:** {job['reason']} ✅")
            st.markdown(f"**✨ 주요 업무:** {job['tasks']} ⚙️")
            st.markdown(f"**🌱 필요 역량 및 준비 과정:** {job['skills']} 📚")
            st.write("---") # 내부 구분선

    st.write(" ")
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 1.1em;'>🤔 이 외에도 궁금한 점이 있으신가요? 챗봇에게 물어보세요! 💬 (추후 업데이트 예정)</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1em;'>💌 MBTI 유형별 성공 스토리 읽어보기! 📚 <a href='#' style='color:#007bff; text-decoration:none;'>[링크]</a></p>", unsafe_allow_html=True)
