# REST was designed to be stateless and for applications to interact with things called resources.

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [] # Remember everytime you restart the app, this list gets cleared because it's an in-memory database. 
           # It only resides in the memory and when you stop the app that memory gets cleared and you losse your data there.

# Api works with resources and every resource has to be a class
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

# Q. What is the most popular http status code ?
# A. It is 200, not 404.

    def post(self, name):
        data = request.get_json()           # This will give an error, If the request doesn't attach a json 
                                            # payload or the request doesn't have a proper Content-Type header. 
                                            # In case you are not sure if your clients are going to give you JSON or not, you can prevent this from giving an error by:
                                            # put "force=True" as argument in get_json and it means you do not need Content-Type header. It will just look into content and it will format it, even if the Content-Type header is not set to application/json. This is nice but is dangerous because it means that without it if you look at the header and if its not set correctly you just do nothng and with it you don't look at the header. Therefore you are always going to do the processing of the text even if its is incorrect. So do't use "force=True".
                                            # The other one that is also quiet handy sometimes is "silent=True" and what this does is it doesn't give an error and it basically returns None. e.g.: request.get_json(silent=True).
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    # We no longer need to do jsonify with flask-restful, because flask-restful does it for us so we can just
    # return dictionaries.

    # Q. What is the http status code for creation ?
    # A. It is 201 (CREATED).

    # Q. What 202 http status code means ?
    # A. 202 means accepted, and the accepted code is when you are delaying the creation. For e.g., if
    # the objct creation takes a long time you may say "I'am gonna create this object, return 202 
    # and the obect gets created then after 5 or 10 minutes". The client doesn't have to wait 5 or 10 minutes,
    # but it knows that you have accepted the creation of that. It may then fail but that's out with
    # the client's control.

    # Using a corret status code is very important because it is a very quick way of clients like 
    # web applications or mobile applications to check whether things went wrong or not. E.g. in the case 
    # of 404 we don't even need to check the payload because we know that nothing's coming back that we are 
    # really interested in. If 201 comes back then we need to check the payload to see what has been created.

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')     # http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)   
# debug = True will show youj a nice html page lets you know what went wrong 
# with your application.