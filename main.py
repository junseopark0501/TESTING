import streamlit as st
import random # 노래 랜덤 추천을 위해

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🎵 오늘의 기분, 어떤 음악으로 채워볼까요?",
    page_icon="🎶",
    layout="wide" # 넓은 레이아웃 사용
)

# --- CSS 스타일링 (더 많은 스타일을 추가할 수 있습니다!) ---
st.markdown("""
<style>
    .main {
        background-image: linear-gradient(to top, #fff1eb 0%, #ace0f9 100%); /* 부드러운 그라데이션 배경 */
    }
    h1 {
        color: #8b008b; /* 보라색 제목 */
        text-align: center;
        font-size: 3.5em;
        text-shadow: 2px 2px #ffc107; /* 밝은 노란색 그림자 */
    }
    h2 {
        color: #ff69b4; /* 핑크색 부제목 */
        text-align: center;
        font-size: 2.5em;
    }
    h3 {
        color: #4682b4; /* 스틸 블루 소제목 */
        font-size: 2em;
    }
    .stSelectbox > div > div > div {
        background-color: #ffffff; /* 드롭다운 배경 흰색 */
        border-radius: 15px;
        border: 2px solid #ff1493; /* 진한 핑크 테두리 */
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        padding: 10px;
        font-size: 1.2em;
    }
    .stButton > button {
        background-image: linear-gradient(to right, #ee0979 0%, #ff6a00 100%); /* 강렬한 그라데이션 버튼 */
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        padding: 15px 30px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 7px 7px 20px rgba(0,0,0,0.4);
    }
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #9370db; /* 연보라 테두리 */
        padding: 10px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.05);
    }
    .song-card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }
    .song-card:hover {
        transform: translateY(-5px);
    }
    .song-card img {
        border-radius: 10px;
        margin-bottom: 15px;
        width: 150px; /* 앨범 아트 크기 조절 */
        height: 150px;
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)

# --- 노래 데이터 (기분별) ---
# 실제 앱에서는 데이터베이스나 CSV 파일에서 불러오는 것이 좋습니다.
# 'album_art_url'은 예시이며, 실제 이미지 URL로 대체해야 합니다.
# 'preview_link'는 Spotify, YouTube 등의 미리 듣기/재생 링크입니다.
song_data = {
    "행복함 😄": {
        "emoji": "☀️",
        "songs": [
            {"title": "Happy", "artist": "Pharrell Williams", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/2/29/Pharrell_Williams_-_Happy.jpg", "preview_link": "https://www.youtube.com/watch?v=y6Sxv-sUYtM", "reason": "듣기만 해도 기분이 좋아지는 긍정 에너지 폭발! ✨"},
            {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/9/91/Mark_Ronson_ft._Bruno_Mars_-_Uptown_Funk.png", "preview_link": "https://www.youtube.com/watch?v=OPf0zY62vM4", "reason": "어깨가 들썩이는 신나는 리듬으로 행복을 만끽하세요! 🕺"},
            {"title": "Dancing Queen", "artist": "ABBA", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/e/e0/ABBA_-_Dancing_Queen.png", "preview_link": "https://www.youtube.com/watch?v=xFrGuyw1V8s", "reason": "클래식 명곡으로 당신의 행복을 더욱 빛나게 해줄 거예요! 👑"}
        ]
    },
    "슬픔 😢": {
        "emoji": "🌧️",
        "songs": [
            {"title": "Someone Like You", "artist": "Adele", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/1/1a/Adele_-_Someone_Like_You.png", "preview_link": "https://www.youtube.com/watch?v=hLQl3WcCc0I", "reason": "감성에 젖어 마음을 정리하고 싶을 때. ☔"},
            {"title": "Hurt", "artist": "Christina Aguilera", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/3/30/Christina_Aguilera_-_Hurt.png", "preview_link": "https://www.youtube.com/watch?v=o0u4M6vKp2k", "reason": "깊은 슬픔을 위로해주는 목소리. 💔"},
            {"title": "Fix You", "artist": "Coldplay", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/d/d4/Coldplay_-_Fix_You.png", "preview_link": "https://www.youtube.com/watch?v=k4V3Mo6S_EFs", "reason": "아픔을 치유하고 다시 일어설 힘을 주는 곡. 🫂"}
        ]
    },
    "신남 🥳": {
        "emoji": "🎉",
        "songs": [
            {"title": "Bohemian Rhapsody", "artist": "Queen", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/9/9f/Queen_Bohemian_Rhapsody.png", "preview_link": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ", "reason": "전설적인 명곡으로 당신의 흥을 폭발시키세요! 🤘"},
            {"title": "Dynamite", "artist": "BTS", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/7/7b/BTS_-_Dynamite.png", "preview_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg", "reason": "글로벌 히트곡으로 신나는 에너지를 느껴보세요! 💥"},
            {"title": "Shape of You", "artist": "Ed Sheeran", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/e/ea/Shape_of_You_Official_Single_Cover.png", "preview_link": "https://www.youtube.com/watch?v=JGwWNGJdvx8", "reason": "중독성 있는 멜로디로 몸을 움직이게 할 거예요! 💃"}
        ]
    },
    "차분함 😌": {
        "emoji": "🧘‍♀️",
        "songs": [
            {"title": "River Flows in You", "artist": "Yiruma", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/d/dc/Yiruma_River_Flows_In_You.jpg", "preview_link": "https://www.youtube.com/watch?v=F-4wR105t0Q", "reason": "잔잔한 피아노 선율로 마음의 평화를 찾아보세요. 🕊️"},
            {"title": "Comptine d'un autre été, l'après-midi", "artist": "Yann Tiersen", "album_art_url": "https://upload.wikimedia.org/wikipedia/en/b/b8/Amelie_soundtrack_cover.jpg", "preview_link": "https://www.youtube.com/watch?v=H2-1LgY76oY", "reason": "아멜리에 OST로 편안하고 아늑한 분위기를 느껴보세요. ☕"},
            {"title": "Canon in D", "artist": "Johann Pachelbel", "album_art_url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Pachelbel_Canon_in_D_cover.jpg", "preview_link": "https://www.youtube.com/watch?v=NlprozGcsyM", "reason": "시대를 초월한 클래식으로 차분함을 더해보세요. 🎶"}
        ]
    }
    # 더 많은 기분과 노래를 여기에 추가할 수 있습니다!
}

# --- 메인 페이지 ---
st.title("🎵 오늘의 기분, 어떤 음악으로 채워볼까요? 🎵")
st.markdown("<h2 style='text-align: center;'>✨ 당신의 마음에 딱 맞는 플레이리스트를 찾아드립니다! ✨</h2>", unsafe_allow_html=True)
st.markdown("---") # 구분선

st.write(" ") # 공백
st.markdown("<p style='text-align: center; font-size: 1.2em;'>👋 당신의 기분을 알려주세요! 그에 맞는 음악을 선물해 드릴게요. 🎁</p>", unsafe_allow_html=True)
st.write(" ") # 공백

col1, col2, col3 = st.columns([1,2,1]) # 가운데 정렬을 위한 컬럼 분할

with col2:
    selected_mood_raw = st.selectbox(
        "🌟 현재 당신의 기분은 어떤가요?",
        list(song_data.keys()),
        index=0,
        help="가장 가까운 기분을 선택해주세요!"
    )
    user_mood_text = st.text_input("📝 직접 기분을 입력해도 좋아요! (예: '오늘 시험 망쳐서 우울해요 😭')", "")

st.write(" ") # 공백

# 세션 상태를 사용하여 기분 선택 여부를 추적
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

if st.button("🚀 플레이리스트 만들기! 🚀"):
    st.session_state.show_results = True

# 노래 추천 페이지 표시
if st.session_state.show_results:
    st.markdown("---") # 구분선

    # 선택된 기분 이름과 이모지 추출 (드롭다운이 우선)
    display_mood_key = selected_mood_raw
    if user_mood_text: # 사용자가 직접 입력한 기분이 있으면 그것을 우선 표시
        display_mood_key = user_mood_text
        # 입력된 텍스트에 맞는 이모지를 찾아 매칭 (고급 기능)
        # 여기서는 단순화를 위해 드롭다운에서 선택된 이모지를 사용하거나, 특정 이모지를 기본으로 사용합니다.
        display_emoji = song_data.get(selected_mood_raw, {}).get("emoji", "🌟")
    else:
        display_emoji = song_data[selected_mood_raw]["emoji"]

    st.markdown(f"<h1 style='color: #a020f0; text-align: center;'>✨ 당신은 **{display_mood_key}** 이시군요! {display_emoji} ✨</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>🎶 **{display_mood_key}**을 위한 추천 플레이리스트! 🎶</h3>", unsafe_allow_html=True)
    st.write(" ")

    # 추천 노래 가져오기 (선택된 기분 또는 기본값)
    if selected_mood_raw in song_data:
        recommended_songs = song_data[selected_mood_raw]["songs"]
    else: # 만약 존재하지 않는 기분이면 기본 행복함 노래를 추천
        recommended_songs = song_data["행복함 😄"]["songs"]

    # 3xN 칼럼으로 노래 카드 배치
    num_cols = 3
    cols = st.columns(num_cols)

    for i, song in enumerate(recommended_songs):
        with cols[i % num_cols]: # 현재 열에 배치
            st.markdown(f"""
            <div class="song-card">
                <img src="{song['album_art_url']}" alt="{song['title']}">
                <p style="font-size: 1.3em; font-weight: bold; color: #333;">{song['title']}</p>
                <p style="font-size: 1em; color: #555;">{song['artist']}</p>
                <p style="font-size: 0.9em; color: #777;">{song['reason']}</p>
                <a href="{song['preview_link']}" target="_blank" style="text-decoration: none;">
                    <button style="
                        background-color: #28a745;
                        color: white;
                        border: none;
                        padding: 8px 15px;
                        border-radius: 10px;
                        font-size: 0.9em;
                        cursor: pointer;
                        margin-top: 10px;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
                        transition: all 0.2s ease;
                    ">▶️ 미리 듣기 🎧</button>
                </a>
            </div>
            """, unsafe_allow_html=True)

    st.write(" ")
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 1.1em;'>🔄 다른 기분으로 다시 추천받고 싶으신가요? 🎶</p>", unsafe_allow_html=True)
    if st.button("⏪ 처음으로 돌아가기"):
        st.session_state.show_results = False # 결과 페이지 숨기고 다시 선택할 수 있게 함
        st.experimental_rerun() # 앱 다시 로드 (초기 상태로)

    st.markdown("<p style='text-align: center; font-size: 1.1em;'>💌 이 플레이리스트가 마음에 드셨나요? 친구에게 공유해주세요! 💖</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.1em;'>💡 당신의 기분과 어울리는 다른 아티스트를 찾아보세요! 🎤</p>", unsafe_allow_html=True)
