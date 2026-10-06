@echo off
cd /d "%~dp0"
echo ============================================================
echo  LTTS Physical AI V&V Console - keep window OPEN, visit:
echo  http://127.0.0.1:8000/
echo  (Ctrl+C to stop the server)
echo ============================================================
if exist "C:\Program Files\Python310\python.exe" (
  "C:\Program Files\Python310\python.exe" backend\server.py
) else (
  py backend\server.py
)
pause

