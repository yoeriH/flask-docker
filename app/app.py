from flask import Flask, jsonify, request, render_template
from config import Config
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from monitor_service import MonitorService


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
monitor_service = MonitorService()

api = Api(app)

@app.route('/dashboard')
def show():
    return render_template('dashboard.html', monitors=monitor_service.all())

@api.route('/status')
class Status(Resource):
    def get(self):
        return {'status': 'ok'}

@api.route('/apps')
class Apps(Resource):
    def get(self):
        return monitor_service.all()

    def post(self):
        return monitor_service.create(request.form['name'])

@api.route('/app/<app_id>')
class AppsStatus(Resource):
    def get(self, app_id):
        return monitor_service.find(app_id)

    def put(self, app_id):
        if not request.form['status']:
            return('status key is required')
        else:
            return monitor_service.update(app_id, request.form['status'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
