from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

# Function to read JSON data
def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

# Function to read CSV data
def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data

# Function to read SQLite data
def read_sqlite(db_path):
    data = []
    if not os.path.exists(db_path):
        print(f"{db_path} not found.")
        return data
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite database: {e}")
    return data

@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id', None)
    error = None
    products_data = []

    # Determine source
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    elif source == 'sql':
        products_data = read_sqlite('products.db')
    else:
        error = "Wrong source"

    # Filter by id if provided
    if product_id and not error:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_data if p['id'] == product_id]
            if not filtered:
                error = "Product not found"
            else:
                products_data = filtered
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=products_data, error=error, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
