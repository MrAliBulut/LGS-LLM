# PowerShell script to start backend and frontend

# Set the working directory to backend
Set-Location -Path "backend"

# Start the backend
Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "-Command uvicorn generate_exam:app --reload" -PassThru

# Return to the root directory
Set-Location -Path ".."

# Wait for the backend to start
Start-Sleep -Seconds 5

# Set the working directory to frontend
Set-Location -Path "frontend"

# Start the frontend
Start-Process -NoNewWindow -FilePath "pnpm.cmd" -ArgumentList "dev"

# Return to the root directory
Set-Location -Path ".."