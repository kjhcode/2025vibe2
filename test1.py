import streamlit as st

# 🌈 앱 기본 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 🎉 타이틀 및 설명
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>✨ MBTI 진로 추천기 ✨</h1>
    <h3 style='text-align: center;'>💡 MBTI 유형에 따라 어울리는 직업을 추천해드려요! 🎓</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# 🧠 MBTI 목록
mbti_types = [
    "INTJ 🧠", "INTP 🧪", "ENTJ 🧭", "ENTP 💡",
    "INFJ 🌈", "INFP 🎨", "ENFJ 💖", "ENFP 🌟",
    "ISTJ 📊", "ISFJ 🛡️", "ESTJ 🏗️", "ESFJ 🤝",
    "ISTP 🛠️", "ISFP 🌿", "ESTP 🚀", "ESFP 🎉"
]

# 🧩 직업 추천 매핑
career_recommendations = {
    "INTJ": ["데이터 과학자 📈", "전략 컨설턴트 🧠", "시스템 엔지니어 🛠️"],
    "INTP": ["연구원 🔬", "AI 개발자 🤖", "철학자 📚"],
    "ENTJ": ["CEO 💼", "프로덕트 매니저 🚀", "경영 컨설턴트 📊"],
    "ENTP": ["벤처 창업가 💡", "광고 기획자 🎯", "기술 분석가 🧪"],
    "INFJ": ["상담가 💬", "작가 ✍️", "심리학자 🧠"],
    "INFP": ["예술가 🎨", "시인 📝", "사회복지사 ❤️"],
    "ENFJ": ["교사 👩‍🏫", "멘토 🤝", "홍보 담당자 📣"],
    "ENFP": ["연예인 🎤", "여행 작가 🌍", "기획자 🧠"],
    "ISTJ": ["회계사 💰", "법률가 ⚖️", "행정공무원 🏢"],
    "ISFJ": ["간호사 🩺", "도서관 사서 📚", "초등교사 👶"],
    "ESTJ": ["프로젝트 매니저 📋", "경찰 👮‍♂️", "군인 🪖"],
    "ESFJ": ["HR 매니저 🤝", "이벤트 플래너 🎈", "상담사 💬"],
    "ISTP": ["정비사 🔧", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP": ["플로리스트 🌸", "사진작가 📷", "디자이너 🎨"],
    "ESTP": ["세일즈 매니저 🛍️", "스턴트 배우 🎬", "투자 분석가 💹"],
    "ESFP": ["MC 🎤", "유튜버 🎥", "패션스타일리스트 👗"]
}

# 🧬 사용자 입력
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", mbti_types)

# 🔍 추천 결과
if selected_mbti:
    mbti_key = selected_mbti[:4]
    st.markdown("---")
    st.subheader(f"🎯 {selected_mbti} 유형에게 추천하는 직업은...")
    for job in career_recommendations[mbti_key]:
        st.markdown(f"- {job}")

    st.markdown("💖 당신의 성향에 맞는 멋진 진로를 찾아가세요!")

# 🦄 푸터
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made with ❤️ by AI | 🌟 꿈을 향해 GO!</div>", unsafe_allow_html=True)
