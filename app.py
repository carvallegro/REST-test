import json

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test', methods=['GET', 'POST'])
def test_rocketchat():
    return json.dumps({
           "text":"HOLa fdfs",
            "attachments": [
                {
                    "title": "Rocket.Chat",
                    "title_link": "https://rocket.chat",
                    "text": "Rocket.Chat, the best open source chat",
                    "image_url": "https://rocket.chat/images/mockup.png",
                    "color": "#764FA5"
                }
            ]
           })

if __name__ == '__main__':
    app.run()


