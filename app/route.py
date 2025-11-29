from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check API
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

# Get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'}
    ]
    return jsonify(items), 200

# Get item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return jsonify({'id': item_id, 'name': f'Item {item_id}'}), 200

# Create item
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    return jsonify({'id': 3, 'name': data.get('name')}), 201

# Update item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    return jsonify({'id': item_id, 'name': data.get('name')}), 200

# Delete item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify({'message': f'Item {item_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)