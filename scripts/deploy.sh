#!/bin/bash

# Example deployment script

# Build frontend assets
echo "Building frontend assets..."
cd frontend/
npm install       # Install npm packages
npm run build     # Build production assets
cd ..

# Perform backend tasks
echo "Setting up backend..."
pip install -r requirements.txt   # Install Python dependencies
python manage.py migrate           # Apply database migrations

# Restart application server
echo "Restarting application server..."
sudo systemctl restart myapp.service   # Replace with your actual service name

echo "Deployment complete!"
