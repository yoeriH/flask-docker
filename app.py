from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'status': 'ok'})


@app.route('/apps')
def index():
    list_of_apps = [{
                'id': 0,
                'name': 'test',
                'size': 3
            } , {
                'id': 1,
                'name': 'booyah',
                'size': 5
            }]

    return jsonify(list_of_apps)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
