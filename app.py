from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Sainsburys',
        'items': [
            {
                'name': 'Bread',
                'price': 1.25

            }
        ]
    }
]


@app.route('/')
def hello_world():
    return 'Hello World!'


# POST - to receive data
# GET - to send data

# POST /store/data:{name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # print('Sainsburys!')
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message:store not found'})


# Pull request TEST
# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item:{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['items']['name'],
                'price': request_data['items']['price']

            }
            store['items'].append(new_item)
        return jsonify(store)
    return jsonify({'message:item not found in store'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message:store not found'})


if __name__ == '__main__':
    app.run()
