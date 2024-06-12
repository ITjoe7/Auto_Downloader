@echo off
REM Start WinSCP with a 5-second delay
    start "WinSCP" "C:\Program Files (x86)\WinSCP\WinSCP.exe"
REM Wait for 5 seconds
    timeout /t 5 /nobreak >nul
REM Run the Python script
    python C:\Users\Joren\Auto_Downloader\Auto_downloader.py
