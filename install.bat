@echo off
setlocal

echo ============================
echo   BZIPMINI INSTALLER
echo ============================

set INSTALL_DIR=%USERPROFILE%\bzp_bin

if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
)

echo Creating bzp command...

(
echo @echo off
echo python "%~dp0cli.py" %%*
) > "%INSTALL_DIR%\bzp.bat"

echo Adding PATH...

powershell -NoProfile -ExecutionPolicy Bypass ^
"[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path','User') + ';%INSTALL_DIR%', 'User')"

echo.
echo Installation complete.
echo.
echo Open a NEW Command Prompt window.
echo.
echo Then test:
echo bzp
echo.

pause
