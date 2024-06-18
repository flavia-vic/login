from flask import Flask
from config import Config
from db import db
from usuarios import models

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True)
