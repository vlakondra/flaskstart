from app import app


@app.route('/special/simple/<string:name>')
def Safe(name):
    return f"Привет {name}!!!!!!"