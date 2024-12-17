@echo off
echo ==============================
echo Iniciando el Backend (Flask)...
echo ==============================
cd C:\Users\Contabilidad\PAGINA_CHPC_2\Backend_CHPC
call venv\Scripts\activate
start cmd /k "python -m flask run"

timeout /t 3 >nul

echo ==============================
echo Iniciando el Frontend (Vue.js)...
echo ==============================
cd C:\Users\Contabilidad\PAGINA_CHPC_2\frontend-chpc
:: Asegurarse de que node y npm estén disponibles
where node >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Node.js no está configurado correctamente en el PATH.
    pause
    exit
)

start cmd /k "npm run serve"

timeout /t 5 >nul
echo ==============================
echo Abriendo el navegador...
echo ==============================

:: Abrir el navegador predeterminado con la URL del frontend
start "" "http://localhost:8080"

echo ==============================
echo Ambos servidores están activos.
pause
