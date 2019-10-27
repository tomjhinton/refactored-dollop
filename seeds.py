from pony.orm import db_session
from app import db
from models.Record import Record
from models.User import User, UserSchema

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():



    schema = UserSchema()




    User(
    username='Admin',
    email='Tomjhinton@gmail.com',
    password_hash=schema.generate_hash('pass'),
    )




    Record(
        artist="First",
        title="Title",
        cover="/images/one.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/two.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/three.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/four.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/five.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/six.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/seven.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/eight.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/nine.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/ten.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/eleven.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )


    Record(
        artist="First",
        title="Title",
        cover="/images/twelve.png",
        description="""Series to the cult groove and the short bass style compositions and producers across the styles of the world of sound are subtle and all the album moves and the steppers of the other instruments in the spiritual, and the title Unit and late ‘80s acts and stares at the style scene and collaboration
        Recorded and studio series and produced by the listeners of the most story heard of their share of ‘The Works’ get the most proof string of ‘Mark One Time’""",
        )



    db.commit()
