from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify([
        {"id": 1, "name": "Product A", "price": 19.99},
        {"id": 2, "name": "Product B", "price": 29.99},
        {"id": 3, "name": "Product C", "price": 39.99}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
