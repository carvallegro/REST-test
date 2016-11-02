from flask import Flask

from src.discourse.access import latest
from src.endpoints.discourse import discourse_blueprint

app = Flask(__name__)
app.register_blueprint(discourse_blueprint, url_prefix='/discourse')


@app.route('/')
def hello_world():
    return latest()


if __name__ == '__main__':
    app.run()
