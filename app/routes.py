from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Привет, World!!!"

@app.route('/test')
def tst():
    a=10

    return str(5/a)+" Привет, World!!!"    