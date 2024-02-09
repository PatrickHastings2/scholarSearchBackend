import os
from flask_cors import CORS
from flask import Flask
from scholarSearchApi import db  # Assuming scholarSearchApi is your package
from scholarSearchApi.api.scholarSearch import scholarSearchBp
from scholarSearchApi.api.data import data_bp
from scholarSearchApi.model.scholarSearch import initScholarSearch
from scholarSearchApi.model.data import initData

app = Flask(__name__)
cors = CORS(app)

# Set the path for the SQLite database in the 'instance' directory
instance_path = os.path.join(app.root_path, 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# SQLite database URI pointing to the 'instance' directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(instance_path, "sqlite.db")

app.register_blueprint(scholarSearchBp)
app.register_blueprint(data_bp)

@app.before_first_request
def init_db():
    print("init")
    with app.app_context():
        db.create_all()
        initScholarSearch()
        initData()

if __name__ == "__main__":
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    with app.app_context():
        init_db()
        app.run(debug=True, host="0.0.0.0", port="8199")

