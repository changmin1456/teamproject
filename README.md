# YOLO 기반 이미지 객체 추출 도구

사진에서 객체를 탐지하고, 선택한 종류의 상자와 개수를 표시하며, 객체별 PNG 미리 보기를 제공하는 팀 프로젝트입니다.

현재 `app.py`는 10주차 실습의 흐름을 참고한 기본 탐지 앱입니다. JPG·PNG를 올리고 **탐지 시작**을 누르면 원본과 탐지 상자가 표시된 이미지를 볼 수 있습니다. 첫 탐지에서 모델 파일이 필요하면 Ultralytics가 자동으로 다운로드합니다. [YOLO11 모델 문서](https://docs.ultralytics.com/models/yolo11/)

## 로컬 환경 설치

Python 3.13을 설치한 뒤 프로젝트 폴더에서 아래 명령을 실행합니다.

macOS / Linux

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

Windows PowerShell

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## 팀원별 작업 계획

| 담당 | 맡을 작업 | 브랜치 예시 |
| --- | --- | --- |
| 1번 | JPG·PNG 업로드와 YOLO 탐지 결과 저장 | `feature/detection` |
| 2번 | 종류별 필터와 원본 이미지의 상자·개수 표시 | `feature/filter` |
| 3번 | 선택한 객체의 PNG 추출과 미리 보기 | `feature/crop-preview` |
| 4번 | Streamlit 화면 통합, 시연용 기능 점검 및 실행 문서 정리 | `feature/integration` |

각 팀원은 자신의 브랜치에서 변경 사항을 커밋하고 푸시한 뒤, `main`을 대상으로 PR을 최소 한 번 엽니다. 팀원이 변경 사항을 리뷰하고 `Python syntax` 검사가 성공하면 병합합니다. 검사에서는 Git이 추적하는 Python 파일의 문법을 확인합니다. 병합 후에는 사람과 자전거가 함께 있는 사진으로 Streamlit에서 상자, 개수, 미리 보기를 직접 확인합니다.
