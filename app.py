import os
from threading import Lock

import streamlit as st
from PIL import Image, ImageOps


@st.cache_resource
def load_model():
    # 실행 중 라이브러리 자동 설치를 끕니다.
    os.environ.setdefault("YOLO_AUTOINSTALL", "false")
    from ultralytics import YOLO

    model = YOLO("yolo11n.pt")
    return model, Lock()


st.title("YOLO 이미지 객체 탐지")
uploaded_file = st.file_uploader(
    "JPG 또는 PNG 이미지 선택", type=["jpg", "jpeg", "png"], max_upload_size=10
)

if uploaded_file is None:
    st.stop()

try:
    with Image.open(uploaded_file, formats=["JPEG", "PNG"]) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        image.thumbnail((1600, 1600))
except (OSError, Image.DecompressionBombError, ImportError):
    st.error("이미지를 읽을 수 없습니다. 정상적인 JPG 또는 PNG 파일을 선택하세요.")
    st.stop()

st.image(image, caption="원본 이미지")

if st.button("탐지 시작"):
    try:
        with st.spinner("사진에서 객체를 찾는 중입니다."):
            model, model_lock = load_model()
            with model_lock:
                results = model.predict(image, conf=0.25, device="cpu", verbose=False)
    except (OSError, RuntimeError):
        st.error("탐지를 실행하지 못했습니다. 모델 파일과 인터넷 연결을 확인하세요.")
        st.stop()

    result = results[0]
    # YOLO가 그린 BGR 이미지를 Streamlit에서 표시할 RGB로 변환합니다.
    result_image = result.plot()[:, :, ::-1]
    st.image(result_image, caption="탐지 결과")
