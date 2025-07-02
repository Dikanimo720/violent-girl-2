# keep_alive.py

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<h1>Bot is awake</h1>'

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()