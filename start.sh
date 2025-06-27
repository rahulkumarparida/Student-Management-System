#!/bin/bash

echo "🚀 Starting server..."
echo "🔁 Running init_db.py every time (temporary fix)..."
python init_db.py

echo "▶️ Starting Flask app using gunicorn..."
gunicorn app:app --bind=0.0.0.0:$PORT
