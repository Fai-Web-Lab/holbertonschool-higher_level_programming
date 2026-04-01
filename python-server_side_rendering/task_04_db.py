import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def get_sql_data(id=None):
    products = []
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if id:
        cursor.execute('SELECT * FROM Products WHERE id = ?', (id,))
    else:
        cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    products = [dict(row) for row in rows]
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            data = get_json_data()
        elif source == 'csv':
            data = get_csv_data()
        elif source == 'sql':
            data = get_sql_data(id_param)
            if id_param and not data:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=data)

        if id_param:
            data = [p for p in data if str(p['id']) == str(id_param)]
            if not data:
                return render_template('product_display.html', error="Product not found")
        
        return render_template('product_display.html', products=data)

    except Exception:
        return render_template('product_display.html', error="Database error")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
