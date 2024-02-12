from flask_cors import CORS
from scholarSearchApi import app, db

from scholarSearchApi.api.login import login_bp
from scholarSearchApi.api.data import data_bp

from scholarSearchApi.model.login import init_login
from scholarSearchApi.model.data import init_data

app.register_blueprint(login_bp)
app.register_blueprint(data_bp)

@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        
        init_login()
        init_data()

if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")
