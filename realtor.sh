#!/bin/bash


# Run the Django server in the background
nohup python manage.py runserver &


# Run the Electron app
npm run realtorhub
