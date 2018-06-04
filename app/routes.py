from app import app, api, monitor_service
from flask import request
from flask_restplus import Api, Resource, fields

@app.route('/dashboard')
def index():
    return 'super slick dashboard'

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
