import sqlite3
from flask import Flask, request, jsonify, render_template_string
app = Flask(__name__)
DB_PATH = 'ecommerce.db'
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT)')
    conn.commit()
    conn.close()
init_db()
@app.route('/')
def home():
    with open('app/static/index.html', 'r') as f:
        return render_template_string(f.read())
@app.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.get_json() or {}
    cart = data.get('cart', [])
    if not cart:
        return jsonify({'error': 'Cart is empty'}), 400
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for item in cart:
        cursor.execute('INSERT INTO orders (item) VALUES (?)', (str(item),))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Order processed successfully!'}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)