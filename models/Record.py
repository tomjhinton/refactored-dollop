from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load
from datetime import datetime, timedelta

from.Order import Order
from.Medium import Medium


class Record(db.Entity):
    artist = Required(str)
    title = Required(str)
    cover = Optional(str)
    description = Required(str)
    orders = Set('Order')
    mediums = Set('Medium')


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    artist = fields.Str(required=True)
    title = fields.Str()
    cover = fields.Str()
    description = fields.Str(required=True)
    orders = fields.Nested('OrderSchema', many=True, dump_only=True)
    mediums = fields.Nested('MediumSchema', many=True, dump_only=True)
