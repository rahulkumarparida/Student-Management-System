#!/bin/bash

# Run init_db.py only once
if [ ! -f ".init_done" ]; then
  echo "Running init_db.py..."
  python init_db.py
  touch .init_done
else
  echo "Skipping init_db.py"
fi

# Start the Flask app with Gunicorn
gunicorn app:app
