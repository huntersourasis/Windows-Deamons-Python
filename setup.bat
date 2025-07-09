@echo off
:: ===============================
:: Daemon Setup Script for Windows
:: Run this script as Administrator
:: ===============================

echo.
echo 📦 Installing required packages...
pip install pywin32

echo.
echo ⚙️ Registering Python service...
python deamon.py install

echo.
echo ▶️ Starting Python service...
python deamon.py start

echo.
echo ✅ Daemon setup complete.
echo.

echo ℹ️ To stop the service, run the following command:
echo     python deamon.py stop
echo.

pause
