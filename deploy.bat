@echo off
REM Cohen House Concierge - Windows SSH/CLI Deployment Script
REM Качване на проекта на отдалечен компютър / Upload project to remote computer
REM Last updated: December 22, 2025

echo ================================================================================
echo   COHEN HOUSE CONCIERGE - WINDOWS DEPLOYMENT SCRIPT
echo   SSH/CLI Upload Tool for Windows
echo ================================================================================
echo.

REM Check if deploy.config exists
if not exist deploy.config (
    echo [ERROR] Deploy configuration file not found!
    echo Creating deploy.config template...
    
    (
    echo # Cohen House Concierge - Deployment Configuration
    echo # Remote server SSH details
    echo REMOTE_USER=your_username
    echo REMOTE_HOST=your_server_ip_or_hostname
    echo REMOTE_PORT=22
    echo REMOTE_PATH=/var/www/concierge
    echo.
    echo # SSH Key ^(optional^)
    echo SSH_KEY_PATH=
    echo.
    echo # Service name
    echo SERVICE_NAME=concierge
    ) > deploy.config
    
    echo [SUCCESS] Created deploy.config
    echo Please edit deploy.config with your server details and run this script again.
    pause
    exit /b 1
)

echo Loading configuration...
for /f "tokens=1,2 delims==" %%a in (deploy.config) do (
    if "%%a"=="REMOTE_USER" set REMOTE_USER=%%b
    if "%%a"=="REMOTE_HOST" set REMOTE_HOST=%%b
    if "%%a"=="REMOTE_PORT" set REMOTE_PORT=%%b
    if "%%a"=="REMOTE_PATH" set REMOTE_PATH=%%b
    if "%%a"=="SSH_KEY_PATH" set SSH_KEY_PATH=%%b
    if "%%a"=="SERVICE_NAME" set SERVICE_NAME=%%b
)

if "%REMOTE_USER%"=="your_username" (
    echo [ERROR] Please configure deploy.config with your server details!
    pause
    exit /b 1
)

echo Remote: %REMOTE_USER%@%REMOTE_HOST%:%REMOTE_PATH%
echo.

REM Check if Git Bash is available (includes SSH and rsync)
where bash >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git Bash is not installed or not in PATH!
    echo.
    echo Please install Git for Windows which includes Git Bash:
    echo https://git-scm.com/download/win
    echo.
    echo Git Bash includes SSH and rsync which are needed for deployment.
    pause
    exit /b 1
)

echo [INFO] Found Git Bash - Good!
echo.

REM Test SSH connection
echo Testing SSH connection...
bash -c "ssh -o ConnectTimeout=5 -p %REMOTE_PORT% %REMOTE_USER%@%REMOTE_HOST% 'echo Connection successful' 2>/dev/null"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Cannot connect to remote server!
    echo.
    echo Please check:
    echo   - Server address and port
    echo   - Username and password/SSH key
    echo   - Network connectivity
    echo.
    pause
    exit /b 1
)

echo [SUCCESS] SSH connection successful
echo.

REM Create backup on remote server
echo Creating backup on remote server...
set BACKUP_NAME=concierge_backup_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_NAME=%BACKUP_NAME: =0%
bash -c "ssh -p %REMOTE_PORT% %REMOTE_USER%@%REMOTE_HOST% 'if [ -d %REMOTE_PATH% ]; then cp -r %REMOTE_PATH% %REMOTE_PATH%_%BACKUP_NAME%; echo Backup created; fi'"
echo [SUCCESS] Remote backup created
echo.

REM Upload files using rsync through Git Bash
echo Starting file upload...
echo This may take a few minutes depending on file size and connection speed...
echo.

bash -c "rsync -avz --progress ^
    --exclude='.git' ^
    --exclude='.gitignore' ^
    --exclude='__pycache__' ^
    --exclude='*.pyc' ^
    --exclude='*.pyo' ^
    --exclude='.env' ^
    --exclude='venv' ^
    --exclude='env' ^
    --exclude='.venv' ^
    --exclude='node_modules' ^
    --exclude='*.log' ^
    --exclude='*.pid' ^
    --exclude='*.db' ^
    --exclude='*.sqlite3' ^
    --exclude='tts_*.mp3' ^
    --exclude='audio_cache' ^
    --exclude='*.backup' ^
    --exclude='*.OLD' ^
    --exclude='*.broken' ^
    --exclude='.DS_Store' ^
    --exclude='*.swp' ^
    --exclude='*.swo' ^
    --exclude='.vscode' ^
    --exclude='.idea' ^
    --exclude='*.pkl' ^
    --exclude='*.dat' ^
    -e 'ssh -p %REMOTE_PORT%' ^
    ./ %REMOTE_USER%@%REMOTE_HOST%:%REMOTE_PATH%/"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Files uploaded successfully!
    echo.
) else (
    echo.
    echo [ERROR] Upload failed!
    pause
    exit /b 1
)

REM Check .env file
echo Checking remote .env configuration...
bash -c "ssh -p %REMOTE_PORT% %REMOTE_USER%@%REMOTE_HOST% 'if [ ! -f %REMOTE_PATH%/.env ]; then echo MISSING; fi'" | findstr "MISSING" >nul
if %ERRORLEVEL% EQU 0 (
    echo [WARNING] No .env file found on remote server!
    echo.
    echo You need to create .env file on the remote server:
    echo   1. SSH to server: ssh %REMOTE_USER%@%REMOTE_HOST%
    echo   2. Go to directory: cd %REMOTE_PATH%
    echo   3. Copy example: cp .env.example .env
    echo   4. Edit file: nano .env
    echo   5. Add your API keys
    echo.
) else (
    echo [SUCCESS] .env file exists on remote server
    echo.
)

REM Install dependencies
echo Installing dependencies on remote server...
bash -c "ssh -p %REMOTE_PORT% %REMOTE_USER%@%REMOTE_HOST% 'cd %REMOTE_PATH% && python3 -m pip install -r requirements.txt --quiet'" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Dependencies installed
) else (
    echo [WARNING] Could not install dependencies automatically
    echo Please SSH to server and run: pip install -r requirements.txt
)
echo.

REM Restart service
echo Restarting service on remote server...
bash -c "ssh -p %REMOTE_PORT% %REMOTE_USER%@%REMOTE_HOST% 'sudo systemctl restart %SERVICE_NAME%'" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Service restarted
) else (
    echo [WARNING] Could not restart service automatically
    echo Please SSH to server and restart manually: sudo systemctl restart %SERVICE_NAME%
)
echo.

REM Final summary
echo ================================================================================
echo [SUCCESS] DEPLOYMENT COMPLETED SUCCESSFULLY!
echo ================================================================================
echo.
echo Next steps:
echo   1. SSH to your server: ssh %REMOTE_USER%@%REMOTE_HOST%
echo   2. Go to directory: cd %REMOTE_PATH%
echo   3. Verify .env file: cat .env
echo   4. Check server status: sudo systemctl status %SERVICE_NAME%
echo   5. View logs: sudo journalctl -u %SERVICE_NAME% -f
echo.
echo Access your application at:
echo   http://%REMOTE_HOST%:8000/solomon.html
echo.
echo Cohen House Concierge deployed! 
echo ================================================================================
echo.
pause
