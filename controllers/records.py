from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Record import Record, RecordSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'records') # creates a router for this controller

@router.route('/records', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many records, ie we expect a list
    schema = RecordSchema(many=True)
    records = Record.select() # get all the records
    return schema.dumps(records) # `schema.dumps` converts the list to JSON


@router.route('/records', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = RecordSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a record object
        record = Record(**data, createdBy=g.current_user)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the record data as JSON
    return schema.dumps(record), 201


@router.route('/records/<int:record_id>', methods=['GET'])
@db_session
def show(record_id):
    # This will serialize our data
    schema = RecordSchema()
    # This gets a record by ID
    record = Record.get(id=record_id)

    # If we can't find a record, send a 404 response
    if not record:
        abort(404)

    # otherwise, send back the record data as JSON
    return schema.dumps(record)


@router.route('/records/<int:record_id>', methods=['PUT'])
@db_session
@secure_route
def update(record_id):
    schema = RecordSchema()
    record = Record.get(id=record_id)

    if not record:
        abort(404)

    try:
        data = schema.load(request.get_json())
        record.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(record)


@router.route('/records/<int:record_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(record_id):
    record = Record.get(id=record_id)

    if not record:
        abort(404)

    record.delete()
    db.commit()

    return '', 204
