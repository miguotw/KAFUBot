from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return '機器人啟動完成，當前版本為:1.5.3'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()