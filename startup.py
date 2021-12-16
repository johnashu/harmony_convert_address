#!/bin/env python3
import os

os.chdir("/app")

# TODO: Find a way to cache the instllation as to not install all dependencies on every start
if os.path.exists("/app/Pipfile.lock"):
    # TODO: Find a way to not pollute the whole cotainer
    os.system("pipenv install --system")

if os.environ.get("INTERFACE") == "WSGI":
    os.system("uvicorn main:app --host 0.0.0.0 --interface wsgi")
else:
    os.system("gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0")
