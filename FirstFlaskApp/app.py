from flask import Flask, jsonify, request, render_template

# Notice flask request is different from requests in Python. 
# The request context allows you to obtain data sent from the client 
# such as a web browser so that you can appropriately handle generating the response.

# A header of an application/call is the first thing that gets analysed by the server to understand what sort of request is this.
# In headers we can say what type of/sort of data we are sending. It is a set of key valuse pairs. e.g. "Content-Type": "application/json"

app = Flask(__name__)  

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ] 
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - Used to receive data
# GET - used to send data back only

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create():
    request_data = request.get_json()   

    # this request is the request that is made to this end point, so when the browser sends us a new request to create a store this request 
    # is that one and the browser will also send us some JSON data which is the name of the store. And this is going to allow us to get 
    # that data back just like it is explained in the request import above

    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # Iterate over stores
    # if the store ,atches, return it
    # If none matche, return an error message

    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})   # to convert stores to a dictionary as json can't be a list
                                         # json always uses double quotes and never single quotes

# POST /store/<string:name>/item (name:, price:)
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(port = 5000) 