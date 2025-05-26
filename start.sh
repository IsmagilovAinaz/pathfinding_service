#!/bin/bash
echo "Starting the path finding service..."
uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT