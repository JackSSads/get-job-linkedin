from flask import Flask
from src.resources import resources

app = Flask(__name__)
app.register_blueprint(resources)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=False)