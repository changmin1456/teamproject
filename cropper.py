from typing import Sequence
import cv2
import numpy as np
from PIL import Image


def _to_rgb_array(image: np.ndarray | Image.Image) -> np.ndarray:
    if isinstance(image, Image.Image):
        return np.array(image.convert("RGB"))
    if not isinstance(image, np.ndarray):
        raise TypeError("image는 numpy.ndarray 또는 PIL.Image.Image여야 합니다.")

    if image.ndim == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    if image.ndim == 3 and image.shape[2] == 4:
        return image[:, :, :3]
    return image


def crop_objects_to_png(
    image: np.ndarray | Image.Image,
    bboxes: Sequence[Sequence[int | float]],
) -> list[bytes]:
    """
    원본 이미지와 (x1, y1, x2, y2) 좌표 목록을 받아
    경계를 보정한 뒤 각 객체를 PNG 바이트 리스트로 반환합니다.
    """
    image_rgb = _to_rgb_array(image)
    if image_rgb.size == 0:
        return []

    h, w = image_rgb.shape[:2]
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    png_list: list[bytes] = []

    for box in bboxes:
        if len(box) != 4:
            continue

        x1, y1, x2, y2 = [int(round(v)) for v in box]

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        x1_c = max(0, min(x1, w))
        y1_c = max(0, min(y1, h))
        x2_c = max(0, min(x2, w))
        y2_c = max(0, min(y2, h))

        if x2_c <= x1_c or y2_c <= y1_c:
            continue

        cropped_bgr = image_bgr[y1_c:y2_c, x1_c:x2_c]
        ok, encoded = cv2.imencode(".png", cropped_bgr)
        if ok:
            png_list.append(encoded.tobytes())

    return png_list
