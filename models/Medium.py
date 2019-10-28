from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load



class Medium(db.Entity):
    name = Required(str)
    record = Set('Record')


class MediumSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    records = fields.Nested('RecordSchema', many=True)
