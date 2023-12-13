from flask_cors import CORS
from jarmi_api import app, db

from jarmi_api.api.souls import souls_bp

from jarmi_api.model.souls import init_souls

app.register_blueprint(souls_bp)

@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        
        init_souls()

if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")