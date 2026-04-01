import json
import csv
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

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            products = read_json('products.json')
        else:
            products = read_csv('products.csv')
    except Exception:
        products = []

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
