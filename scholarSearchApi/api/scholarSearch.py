from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.scholarSearch import ScholarSearch

scholarSearchBp = Blueprint("scholarSearch", __name__)
scholarSearchApi = Api(scholarSearchBp)

class ScholarSearchAPI(Resource):
    def get(self):
        id = request.args.get("id")
        scholarSearch = db.session.query(ScholarSearch).get(id)
        if scholarSearch:
            return scholarSearch.to_dict()
        return {"message": "not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("password", required=True, type=str)
        args = parser.parse_args()
        scholarSearch = ScholarSearch(args["username"], args["password"])

        try:
            db.session.add(scholarSearch)
            db.session.commit()
            return scholarSearch.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message":f"error {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("username")
        parser.add_argument("password")
        args = parser.parse_args()
        
        try:
            scholarSearch = db.session.query(ScholarSearch).get(args["id"])
            if scholarSearch:
                if args["username"] is not None:
                    scholarSearch.username = args["username"]
                if args["password"] is not None:
                    scholarSearch.password = args["password"]
                db.session.commit()
                return scholarSearch.to_dict(), 200
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
            scholarSearch = db.session.query(ScholarSearch).get(args["id"])
            if scholarSearch:
                db.session.delete(scholarSearch)
                db.session.commit()
                return scholarSearch.to_dict()
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

class ScholarSearchListAPI(Resource):
    def get(self):
        scholarSearch = db.session.query(ScholarSearch).all()
        return [scholarSearch.to_dict() for scholar in scholarSearch]
    
    def delete(self):
        try:
            db.session.query(ScholarSearch).delete()
            db.session.commit()
            return
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}

scholarSearchApi.add_resource(ScholarSearchAPI, "/scholarSearch")
scholarSearchApi.add_resource(ScholarSearchListAPI, "/scholarSearchList")