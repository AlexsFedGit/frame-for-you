import sys
import os
INTERP = os.path.expanduser("~/venv310/bin/python3")

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

from config.wsgi import application
