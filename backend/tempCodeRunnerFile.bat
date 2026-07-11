@echo off
setlocal
set "PY_EXE=C:\Users\Lenovo\anaconda3\python.exe"
set "APP_DIR=%~dp0"
set "APP_DIR=%APP_DIR:~0,-1%"
set "APP_SCRIPT=%APP_DIR%\inventory_system.py"
set "APP_URL=http://127.0.0.1:5000"

if not exist "%PY_EXE%" (
    where py >nul 2>nul
    if errorlevel 1 (
        echo Python not found at: %PY_EXE%
        echo Also could not find the Python launcher ^(py^) in PATH.
        pause
        exit /b 1
    )
    set "PY_EXE=py -3"
)

if not exist "%APP_SCRIPT%" (
    echo Backend script not found at: %APP_SCRIPT%
    pause
    exit /b 1
)

start "Inventory Backend" cmd /k "cd /d "%APP_DIR%" && %PY_EXE% "%APP_SCRIPT%""
timeout /t 2 /nobreak >nul
start "" "%APP_URL%"

endlocal