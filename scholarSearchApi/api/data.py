from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.data import Data

data_bp = Blueprint("data", __name__)
data_api = Api(data_bp)

class DataAPI(Resource):
    def get(self):
        id = request.args.get("id")
        data = db.session.query(Data).get(id)
        if data:
            return data.to_dict()
        return {"message": "not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("password", required=True, type=str)
        args = parser.parse_args()
        data = Data(args["username"], args["password"])

        try:
            db.session.add(data)
            db.session.commit()
            return data.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("username")
        parser.add_argument("password")
        args = parser.parse_args()
        
        try:
            data = db.session.query(Data).get(args["id"])
            if data:
                if args["username"] is not None:
                    data.username = args["username"]
                if args["password"] is not None:
                    data.password = args["password"]
                db.session.commit()
                return data.to_dict(), 200
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            data = db.session.query(Data).get(args["id"])
            if data:
                db.session.delete(data)
                db.session.commit()
                return data.to_dict()
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

class DataListAPI(Resource):
    def get(self):
        data = db.session.query(Data).all()
        return [datum.to_dict() for datum in data]
    
    def delete(self):
        try:
            db.session.query(Data).delete()
            db.session.commit()
            return
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}

data_api.add_resource(DataAPI, "/data")
data_api.add_resource(DataListAPI, "/dataList")
