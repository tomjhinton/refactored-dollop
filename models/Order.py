from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load

from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load
from datetime import datetime, timedelta


class Order(db.Entity):
    records = Set('Record')


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    records = fields.Nested('RecordSchema', many=True, exclude=('orders',))
