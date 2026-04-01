import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def read_csv(filepath):
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        rows = cursor.fetchall()
      products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error:
        return None
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    products = []
    
    if source == 'json':
        try:
            products = read_json('products.json')
        except Exception:
            return render_template('product_display.html', error="File not found")
            
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception:
            return render_template('product_display.html', error="File not found")
            
    elif source == 'sql':
        products = read_sql(product_id)
        if products is None:
            return render_template('product_display.html', error="Database error")
        if product_id and not products:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)

    if product_id:
        try:
            p_id = int(product_id)
            products = [p for p in products if p['id'] == p_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
