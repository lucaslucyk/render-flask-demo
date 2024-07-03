from flask import Flask, jsonify
from .database import DbSession
from .conf import settings


app = Flask(__name__)


@app.get("/")
def index():
    return {"ping": "pong"}


@app.get("/samples")
def list_samples():

    with DbSession(settings.DB_URL) as session:
        session.execute("SELECT * FROM sample")
        samples = session.fetchall()

    return jsonify(samples)


if __name__ == "__main__":
    app.run()
