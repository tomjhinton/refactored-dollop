from pony.orm import db_session
from app import db
from models.Record import Record
from models.User import User, UserSchema

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():



    schema = UserSchema()




    Admin = User(
    name='Admin',
    email='Tomjhinton@gmail.com',
    password_hash=schema.generate_hash('pass'),
    )




    Record(
        artist="First",
        title="Title",
        cover="src/images/one.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )





    db.commit()
