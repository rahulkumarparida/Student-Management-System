#!/bin/bash

# Run init_db only once — create a marker file after it runs
if [ ! -f ".init_done" ]; then
  echo "Running init_db.py for the first time..."
  python init_db.py
  touch .init_done
else
  echo "init_db.py already ran. Skipping..."
fi

# Start the web server
gunicorn app:app
