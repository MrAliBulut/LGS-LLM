# PowerShell script to start backend and frontend

# Start the backend
Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "-Command uvicorn generate_exam:app --reload" -PassThru

# Wait for the backend to start
Start-Sleep -Seconds 5

# Start the frontend
Start-Process -NoNewWindow -FilePath "pnpm.cmd" -ArgumentList "dev"