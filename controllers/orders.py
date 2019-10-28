from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Order import Order, OrderSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'orders') # creates a router for this controller

@router.route('/orders', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many orders, ie we expect a list
    schema = OrderSchema(many=True)
    orders = Order.select() # get all the orders
    return schema.dumps(orders) # `schema.dumps` converts the list to JSON


@router.route('/orders', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = OrderSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a order object
        order = Order(**data)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the order data as JSON
    return schema.dumps(order), 201


@router.route('/orders/<int:order_id>', methods=['GET'])
@db_session
def show(order_id):
    # This will serialize our data
    schema = OrderSchema()
    # This gets a order by ID
    order = Order.get(id=order_id)

    # If we can't find a order, send a 404 response
    if not order:
        abort(404)

    # otherwise, send back the order data as JSON
    return schema.dumps(order)


@router.route('/orders/<int:order_id>', methods=['PUT'])
@db_session
@secure_route
def update(order_id):
    schema = OrderSchema()
    order = Order.get(id=order_id)

    if not order:
        abort(404)

    try:
        data = schema.load(request.get_json())
        order.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(order)


@router.route('/orders/<int:order_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(order_id):
    order = Order.get(id=order_id)

    if not order:
        abort(404)

    order.delete()
    db.commit()

    return '', 204
