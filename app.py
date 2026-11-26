
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="객체 탐지 스튜디오",
    page_icon="📷",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100%;
    }

    [data-testid="stSidebar"] {
        min-width: 250px;
        max-width: 250px;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 700;
        margin-top: 15px;
    }

    div[data-testid="stMetric"] {
        background: #f7f8fa;
        padding: 18px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown('<div class="sidebar-title">📷 객체 탐지 스튜디오</div>',
                unsafe_allow_html=True)

    st.caption("IMAGE ANALYSIS")
    st.markdown("---")

    menu = {
        "이미지 업로드": "upload",
        "탐지 결과 정보": "result",
        "이미지 비교": "comparison",
        "객체 선택 및 추출": "extraction",
        "탐지 요약": "summary",
        "결과 다운로드": "download"
    }

    for name, section_id in menu.items():
        st.markdown(
            f'<a href="#{section_id}" target="_self" '
            f'style="display:block; padding:12px 10px; '
            f'text-decoration:none; color:inherit; '
            f'border-radius:7px;">{name}</a>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.caption("YOLO + OpenCV")

# 메인 화면
st.title("객체 탐지 스튜디오")
st.caption("YOLO 및 OpenCV 기반 이미지 분석 프로그램")

st.divider()

# 1. 이미지 업로드
st.markdown('<div id="upload"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">1. 이미지 업로드</div>',
            unsafe_allow_html=True)

st.write("분석할 이미지를 업로드하세요.")

uploaded_file = st.file_uploader(
    "이미지를 드래그하거나 파일을 선택하세요.",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.success(f"업로드 완료: {uploaded_file.name}")
    st.image(uploaded_file, use_container_width=True)

detect_button = st.button(
    "객체 탐지 시작",
    type="primary",
    use_container_width=True,
    disabled=uploaded_file is None
)

st.divider()

# 2. 탐지 결과 정보
st.markdown('<div id="result"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">2. 탐지 결과 정보</div>',
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("탐지 객체 수", "0개")

with col2:
    st.metric("객체 종류", "0개")

with col3:
    st.metric("처리 상태", "대기")

st.divider()

# 3. 이미지 비교
st.markdown('<div id="comparison"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">3. 이미지 비교</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("**원본 이미지**")
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
    else:
        st.info("이미지를 업로드해주세요.")

with col2:
    st.write("**객체 탐지 결과**")
    st.info("탐지 결과 이미지가 표시됩니다.")

st.divider()

# 4. 객체 선택 및 추출
st.markdown('<div id="extraction"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">4. 객체 선택 및 추출</div>',
            unsafe_allow_html=True)

detected_objects = []

if detected_objects:
    selected_object = st.selectbox(
        "추출할 객체를 선택하세요.",
        detected_objects
    )

    st.button(
        "선택한 객체 추출하기",
        type="primary",
        use_container_width=True
    )
else:
    st.info("객체 탐지를 진행하면 실제 탐지된 객체 목록이 표시됩니다.")

st.write("**추출 결과 미리보기**")
st.info("선택한 객체의 추출 이미지가 표시됩니다.")

st.divider()

# 5. 탐지 요약
st.markdown('<div id="summary"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">5. 탐지 요약</div>',
            unsafe_allow_html=True)

st.info("탐지된 객체의 이름과 신뢰도 등의 상세 정보가 표시됩니다.")

st.divider()

# 7. 결과 다운로드
st.markdown('<div id="download"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">7. 결과 다운로드</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("**탐지 결과 이미지**")
    st.button(
        "탐지 이미지 다운로드",
        use_container_width=True,
        disabled=True
    )

with col2:
    st.write("**추출 객체 이미지**")
    st.button(
        "추출 이미지 다운로드",
        use_container_width=True,
        disabled=True
    )

st.divider()
st.caption("객체 탐지 스튜디오 | YOLO 및 OpenCV")
