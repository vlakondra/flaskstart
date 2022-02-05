from flask import Flask

app = Flask(__name__)
print('app? ', app)

from app import routes