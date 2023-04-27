#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    

    bakeries = []

    for bakery in Bakery.query.all():
        result = bakery.to_dict()
        bakeries.append(result)
    
    # bakery_dict = {
    #     "name": Bakery.query.first().name
    # }

    response = make_response(jsonify(bakeries), 200)
    response.headers['Content-Type'] = 'application/json'
    

    # response = make_response(jsonify(bakeries), 200, {"Content-Type": "application/json"})
    # return response

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):

    bakery = Bakery.query.filter_by(id=id).first()
    bakery_serialized = bakery.to_dict()

    response = make_response(
        jsonify(bakery_serialized),
        200
    )
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    
    goods = []
    for good in BakedGood.query.order_by(BakedGood.price).all():
        goods.append(good.to_dict())

    response = make_response(goods, 200)
    # response.headers["Content-Type"] = "application/json"
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    good = BakedGood.query.order_by(BakedGood.price).all()[-1]
    good_dict = good.to_dict()

    response = make_response(jsonify(good_dict), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run(port=555, debug=True)
