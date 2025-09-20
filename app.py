from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/songs.json')
def songs():
    return send_from_directory('.', 'songs.json')

if __name__ == '__main__':
    # Serve localmente para testes
    app.run(debug=True)