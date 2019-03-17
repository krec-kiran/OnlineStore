from flask import Flask

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
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # print('Sainsburys!')
    pass


# Pull request TEST
# GET /store
@app.route('/store')
def get_stores():
    pass


# POST /store/<string:name>/item:{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


if __name__ == '__main__':
    app.run()
