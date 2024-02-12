import sys
import subprocess
from gunicorn.app.wsgiapp import run

def update_and_install_tmate():
    subprocess.call(["sudo", "apt", "update"])
    subprocess.call(["sudo", "apt", "install", "tmate"])

def run_speedtest():
    subprocess.call(["pip3", "install", "speedtest-cli"])
    speedtest_output = subprocess.check_output(["speedtest-cli"]).decode("utf-8")
    print(speedtest_output)

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    update_and_install_tmate()
    run_speedtest()
    sys.exit(run())
