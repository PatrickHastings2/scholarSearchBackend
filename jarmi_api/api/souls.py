from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.souls import Souls

souls_bp = Blueprint("souls", __name__)
souls_api = Api(souls_bp)

class SoulsAPI(Resource):
    def get(self):
        id = request.args.get("id")
        souls = db.session.query(Souls).get(id)
        if souls:
            return souls.to_dict()
        return {"message": "not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("class_name", required=True, type=str)
        parser.add_argument("health", required=True, type=int)
        parser.add_argument("attack", required=True, type=int)
        parser.add_argument("resistance", required=True, type=int)
        parser.add_argument("power", required=True, type=int)
        args = parser.parse_args()
        souls = Souls(args["class_name"], args["health"], args["attack"], args["resistance"], args["power"])

        try:
            db.session.add(souls)
            db.session.commit()
            return souls.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message":f"error {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("class_name", type=str)
        parser.add_argument("health", type=int)
        parser.add_argument("attack", type=int)
        parser.add_argument("resistance", type=int)
        parser.add_argument("power", type=int)
        args = parser.parse_args()
        
        try:
            souls = db.session.query(Souls).get(args["id"])
            if souls:
                if args["class_name"] is not None:
                    souls.class_name = args["class_name"]
                if args["health"] is not None:
                    souls.health = args["health"]
                if args["attack"] is not None:
                    souls.attack = args["attack"]
                if args["resistance"] is not None:
                    souls.resistance = args["resistance"]
                if args["power"] is not None:
                    souls.power = args["power"]
                db.session.commit()
                return souls.to_dict(), 200
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
            souls = db.session.query(Souls).get(args["id"])
            if souls:
                db.session.delete(souls)
                db.session.commit()
                return souls.to_dict()
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

class SoulsListAPI(Resource):
    def get(self):
        souls = db.session.query(Souls).all()
        return [soul.to_dict() for soul in souls]

souls_api.add_resource(SoulsAPI, "/souls")
souls_api.add_resource(SoulsListAPI, "/soulsList")