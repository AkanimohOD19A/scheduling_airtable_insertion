@echo off
echo Starting Airtable Automated Data Ingestion Service...

:: Project directory
cd /d C:\Users\buasc\PycharmProjects\scrapEngineering

:: Activate virtual environment
call C:\Users\buasc\PycharmProjects\scrapEngineering\venv_airtable\Scripts\activate.bat

:: Run python script
python ingestData.py

:: Keep the window open if there's no error
if %ERRORLEVEL% NEQ 0 (
    echo An error ocurred! Error code: %ERRORLEVEL%
    pause
)