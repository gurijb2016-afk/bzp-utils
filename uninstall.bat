@echo off
echo ============================
echo   bzp utils UNINSTALLER
echo ============================

set INSTALL_DIR=%USERPROFILE%\bzp_bin

if exist "%INSTALL_DIR%\bzp.bat" (
    del "%INSTALL_DIR%\bzp.bat"
)

if exist "%INSTALL_DIR%" (
    rmdir "%INSTALL_DIR%"
)

echo.
echo NOTE:
echo A PATH bejegyzést kézzel kell eltávolítani, ha hozzáadtad.
echo.

pause
