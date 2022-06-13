@echo off
cmd /k "cd /d %cd%\venv\Scripts & activate & cd /d %cd% & python manage.py runserver"