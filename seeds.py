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





    Record(
        name="Python pic 1",
        picture="https://66.media.tumblr.com/2e27aafca3635fc39ed986936b50379e/tumblr_ps9jc4j0UH1w3debko1_1280.png",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique neque ut accumsan tristique. Cras leo felis, semper in eleifend placerat, efficitur a nunc. Morbi fringilla egestas ante, vitae lacinia nunc vestibulum vitae. Mauris auctor dui eget gravida viverra. Pellentesque vel ultricies diam, sit amet dapibus leo. Morbi mattis enim elit, a imperdiet augue tempor ut. Suspendisse suscipit eleifend dui, bibendum consectetur arcu tristique vel. Nam nec risus aliquet, porttitor quam nec, ultrices sapien. Etiam in iaculis enim. Morbi ultricies semper arcu, vel luctus nulla iaculis auctor. Praesent vitae augue vitae lectus ultrices venenatis sit amet non dolor. Fusce dapibus dignissim nulla sit amet lacinia. Fusce non tortor ac quam vestibulum viverra. Praesent a lectus et dolor consequat aliquet vitae non turpis. Nullam et nulla vitae mi ultrices viverra. Integer sodales arcu velit, a faucibus neque dapibus ut.\n\n

        Curabitur tempus risus sit amet mi finibus mattis. Quisque gravida tempor tortor at consequat. Duis vulputate interdum leo id congue. Maecenas rhoncus nec ligula ut malesuada. Pellentesque volutpat felis ligula, vitae dapibus augue faucibus a. Aenean sagittis enim at quam accumsan, a varius lectus dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut imperdiet arcu ipsum, et porttitor velit scelerisque ut. Vivamus vitae semper mi, eu efficitur neque.""",
        )





    db.commit()
