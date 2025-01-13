#!/bin/bash

# Start FastAPI backend
echo "Starting FastAPI backend..."
PYTHONPATH=$PYTHONPATH:. uvicorn ai_shadow.dashboard.app:app --reload --port 8000 &

# Wait for backend to start
sleep 2

# Open Live Server
echo "Starting Live Server..."
code --install-extension ritwickdey.LiveServer
code . --goto ai_shadow/dashboard/templates/dashboard.html

echo "Development servers started!"
echo "Backend running at: http://localhost:8000"
echo "Frontend will be available through Live Server (right-click dashboard.html and select 'Open with Live Server')" 