from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
app = Flask(__name__)
Talisman.init_app(app, content_security_policy=None)
CORS(app, resources={r"/*": {"origins": "*"}})