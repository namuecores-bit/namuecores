# Bycle Manager

간단한 PyQt6 기반 자전거 관리 앱입니다. SQLite3 데이터베이스(`bycle.db`)에 `Bycle` 테이블을 만들고 초기 100개의 데이터를 시드합니다.

실행 방법:

Windows에서 가상환경을 만들고 실행하세요:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python BycleManager.py
```

기능:
- 추가, 수정, 삭제, 검색
- 하단 `QTableWidget`에 리스트 출력
- 간단한 스타일 적용
