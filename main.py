from flask_cors import CORS
from scholarSearchApi import app, db

from scholarSearchApi import scholarSearchBp

from scholarSearchApi.model.scholarSearch import initScholarSearch

app.register_blueprint(scholarSearchBp)

@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        
        initScholarSearch()

if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")