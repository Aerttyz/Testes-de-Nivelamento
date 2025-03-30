from flask import Flask
from config import Config
from database import db
from routes.demonstracoes_contabeis_router import demonstracoes_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/teste'

db.init_app(app)

app.register_blueprint(demonstracoes_bp)
if __name__ == "__main__":
    app.run(debug=True)