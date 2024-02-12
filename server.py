import sys
from gunicorn.app.wsgiapp import run

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app && python3 bot.py".split()
    sys.exit(run())
