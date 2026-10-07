# Drill #9 — 소년 상하좌우 및 대각선 이동

## 실행

Python과 `pico2d`가 설치된 환경에서 이 폴더를 작업 디렉터리로 열고 실행한다.

```bash
python Drill09_movement.py
```

## 조작

- 방향키: 상하좌우 이동
- 수직 방향키와 수평 방향키 동시 입력: 대각선 이동
- Esc 또는 창 닫기: 종료

정지 시 IDLE 애니메이션이 재생된다. 위아래로만 이동할 때는 마지막 좌우 방향을 유지한다. 화면 경계에서는 소년 이미지 전체가 화면 안에 남는다.

## 검증

```bash
python -m unittest discover -s tests -v
```

게임은 `Drill09_movement.py`, 화면과 분리된 이동 및 애니메이션 상태는 `boy_movement.py`에 있다. 기존 수업 예제 파일은 수정하지 않았다.
