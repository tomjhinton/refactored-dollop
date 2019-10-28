import os
from app import app
from controllers import  users, records, orders


app.register_blueprint(users.router, url_prefix='/api')

app.register_blueprint(records.router, url_prefix='/api')

app.register_blueprint(orders.router, url_prefix='/api')



@app.route('/') # homepage
@app.route('/<path:path>') # any other path
def catch_all(path='index.html'):

    if os.path.isfile('dist/' + path): # if path is a file, send it back
        return app.send_static_file(path)

    return app.send_static_file('index.html') # otherwise send back the index.html file
