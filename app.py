from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
api = Api(app)

@api.route('/status')
class Status(Resource):
    def get(self):
        return {'status': 'ok'}

@api.route('/apps')
class Apps(Resource):
    def get(self):
        list_of_apps = [{
                    'id': 0,
                    'name': 'test',
                    'size': 3
                } , {
                    'id': 1,
                    'name': 'booyah',
                    'size': 5
                }]
        return list_of_apps

@api.route('/app/<app_id>')
class AppsStatus(Resource):
    def get(self, app_id):
        return jsonify({'status': 'ok', 'app_id': app_id})

    def put(self, app_id):
        return({'app_id': app_id, 'registered': True})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
