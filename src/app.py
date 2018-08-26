from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/js/<path:filename>')
def send_css(filename):
    return send_from_directory('../static/css', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('../static/js', filename)

if __name__ == "__main__":
    app.run(debug=True)
