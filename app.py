
import streamlit as st

st.set_page_config(
    page_title="객체 탐지 스튜디오",
    page_icon="📷",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        font-size: 32px;
        font-weight: 700;
    }

    div.stButton > button {
        border-radius: 8px;
        height: 45px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.title("📷 객체 탐지 스튜디오")
st.caption("YOLO 및 OpenCV 기반 이미지 객체 탐지 프로그램")

st.divider()

# 탐지 결과 저장 공간
if "detected_objects" not in st.session_state:
    st.session_state.detected_objects = []

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "전체"

# 1. 이미지 업로드
st.subheader("이미지 업로드")

uploaded_file = st.file_uploader(
    "분석할 이미지를 업로드하세요.",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.success(f"업로드 완료: {uploaded_file.name}")

    st.image(
        uploaded_file,
        caption="업로드한 원본 이미지",
        use_container_width=True
    )

detect_button = st.button(
    "객체 탐지 시작",
    type="primary",
    use_container_width=True,
    disabled=uploaded_file is None
)

if detect_button:
    st.info("YOLO 탐지 기능 연결 대기 중입니다.")

st.divider()

# 2. 객체 종류별 필터
st.subheader("객체 종류")

categories = ["전체", "자전거", "사람", "자동차"]

columns = st.columns(4)

for i, category in enumerate(categories):
    with columns[i]:
        if st.button(
            category,
            key=f"category_{category}",
            type=(
                "primary"
                if st.session_state.selected_category == category
                else "secondary"
            ),
            use_container_width=True
        ):
            st.session_state.selected_category = category
            st.rerun()

st.divider()

# 3. 선택한 객체 이미지 표시
selected_category = st.session_state.selected_category

st.subheader(f"{selected_category} 탐지 결과")

# 팀원 YOLO/OpenCV 코드와 연결할 데이터
detected_objects = st.session_state.detected_objects

# 선택한 종류에 따라 객체 필터링
if selected_category == "전체":
    filtered_objects = detected_objects
else:
    filtered_objects = [
        obj for obj in detected_objects
        if obj["name"] == selected_category
    ]

# 탐지 결과 이미지 표시
if filtered_objects:
    columns = st.columns(3)

    for i, obj in enumerate(filtered_objects):
        with columns[i % 3]:
            st.image(
                obj["image"],
                caption=f'{obj["name"]} ({obj["confidence"]:.1%})',
                use_container_width=True
            )

else:
    if not uploaded_file:
        st.info("먼저 이미지를 업로드해주세요.")
    elif not detected_objects:
        st.info("객체 탐지를 진행하면 결과 이미지가 표시됩니다.")
    else:
        st.info("선택한 종류의 탐지 결과가 없습니다.")

st.divider()

st.caption("객체 탐지 스튜디오 | YOLO + OpenCV")
