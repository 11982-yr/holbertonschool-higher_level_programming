from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")
DB_PATH = os.path.join(BASE_DIR, "products.db")


def read_products_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        return []

    products = []
    for item in data:
        if isinstance(item, dict):
            products.append({
                "id": int(item.get("id")) if str(item.get("id", "")).isdigit() else item.get("id"),
                "name": item.get("name"),
                "category": item.get("category"),
                "price": float(item.get("price")) if item.get("price") is not None else None
            })
    return products


def read_products_csv(filepath):
    products = []
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row.get("id", "")
            products.append({
                "id": int(pid) if str(pid).isdigit() else pid,
                "name": row.get("name"),
                "category": row.get("category"),
                "price": float(row.get("price")) if row.get("price") not in (None, "") else None
            })
    return products


def read_products_sqlite(db_path):
    products = []
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    for r in rows:
        products.append({
            "id": int(r[0]),
            "name": r[1],
            "category": r[2],
            "price": float(r[3])
        })

    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id", None)

    error = None
    products_list = []

    # Load products based on source
    try:
        if source == "json":
            products_list = read_products_json(JSON_PATH)
        elif source == "csv":
            products_list = read_products_csv(CSV_PATH)
        elif source == "sql":
            products_list = read_products_sqlite(DB_PATH)
        else:
            return render_template("product_display.html", products=[], error="Wrong source")

    except FileNotFoundError:
        return render_template("product_display.html", products=[], error="Data file not found")
    except sqlite3.Error:
        return render_template("product_display.html", products=[], error="Database error")
    except (json.JSONDecodeError, ValueError):
        return render_template("product_display.html", products=[], error="Error reading data")

    # Filter by id if provided
    if id_param is not None:
        if not str(id_param).isdigit():
            return render_template("product_display.html", products=[], error="Product not found")

        wanted_id = int(id_param)
        filtered = [p for p in products_list if p.get("id") == wanted_id]

        if not filtered:
            return render_template("product_display.html", products=[], error="Product not found")

        products_list = filtered

    return render_template("product_display.html", products=products_list, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
