from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Bienvenue sur mon API Flask !"

@app.route('/api/hello')
def hello():
    return {"message": "Hello depuis Flask", "status": "ok"}

@app.route('/api/status')
def status():
    return {"status": "en ligne", "version": "1.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)