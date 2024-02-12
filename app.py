from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_endpoint():
    return 'Server is up'

@app.route('/run', methods=['GET'])
def run_command():
    cmd = request.args.get('cmd', '')
    if not cmd:
        return 'No command provided'

    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

if __name__ == '__main__':
    app.run()
