from models import db, entry, person
from flask import Flask, send_from_directory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/gabebook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

STATIC_DIR = '../static'

with app.app_context():
    db.init_app(app)
    #db.create_all()

@app.route('/')
def home():
    return send_from_directory(STATIC_DIR + '/html', 'index.html')

@app.route('/api/v1/p')
def people():
    if request.method == 'POST':
        # parse body, create a new entry, return new person
        return ''
    elif request.method == 'PUT':
        # parse body, find person, update entry, return updated person
        return ''
    else:
        return ''

@app.route('/api/v1/p/<int:person>')
def person(person):
    if request.method == 'GET':
        return ''
    else:
        return ''

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory(STATIC_DIR+'/css', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory(STATIC_DIR+'/js', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)
