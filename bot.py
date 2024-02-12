from pyrogram import Client, filters
import subprocess

# Fill in your bot token, api_id, and api_hash
api_id = 9907811
api_hash = "b5adb7f7d4a096750edec1bc6daacd56"
bot_token = "6072139735:AAHr5Lim0mx27SDqJfBGD-4-kFoGK8cbI7c"

# Create a Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a handler for the /run command
@app.on_message(filters.command("run") & filters.private)
def run_command(client, message):
    # Extract the command from the message
    command = message.text.split(maxsplit=1)[1]
    
    # Execute the command
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    # Send the result back to the user
    message.reply_text(result)

# Start the bot
app.run()
