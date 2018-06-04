from flask import Flask, jsonify
from config import Config
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

from app import routes
