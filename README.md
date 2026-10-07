# Drill #9 — 소년 상하좌우 및 대각선 이동

## 실행

이 프로젝트는 `pico2d`를 사용한다. Windows PowerShell에서 프로젝트 폴더를 연 뒤 처음 한 번 환경을 준비한다.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

VS Code에서 `Python: Select Interpreter`를 실행해 `.venv\Scripts\python.exe`를 선택한다. 프로젝트의 `.vscode/settings.json`에도 이 경로가 기본 인터프리터로 지정돼 있다.

이 컴퓨터에는 전역 Python 3.13에 `pico2d`가 이미 설치돼 있어, 현재 생성된 `.venv`는 전역 패키지를 공유하도록 구성했다. 다른 컴퓨터에서는 위 명령으로 독립적인 가상 환경을 만들고 패키지를 설치하면 된다. 이미지 경로는 실행 파일의 위치를 기준으로 찾는다.

```powershell
.\.venv\Scripts\python.exe Drill09_movement.py
```

## 조작

- 방향키: 상하좌우 이동
- 수직 방향키와 수평 방향키 동시 입력: 대각선 이동
- Esc 또는 창 닫기: 종료

정지 시 IDLE 애니메이션이 재생된다. 위아래로만 이동할 때는 마지막 좌우 방향을 유지한다. 화면 경계에서는 소년 이미지 전체가 화면 안에 남는다.

## 검증

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

게임은 `Drill09_movement.py`, 화면과 분리된 이동 및 애니메이션 상태는 `boy_movement.py`에 있다. 기존 수업 예제 파일은 수정하지 않았다.
