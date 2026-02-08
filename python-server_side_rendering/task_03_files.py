from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "products.json")
CSV_PATH = os.path.join(BASE_DIR, "products.csv")


def read_products_json(filepath):
    """Return a list of product dicts from a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Expecting a list of dicts
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
    """Return a list of product dicts from a CSV file."""
    products = []
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert fields
            pid = row.get("id", "")
            products.append({
                "id": int(pid) if str(pid).isdigit() else pid,
                "name": row.get("name"),
                "category": row.get("category"),
                "price": float(row.get("price")) if row.get("price") not in (None, "") else None
            })
    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id", None)

    error = None
    products_list = []

    # Validate source + load correct file
    try:
        if source == "json":
            products_list = read_products_json(JSON_PATH)
        elif source == "csv":
            products_list = read_products_csv(CSV_PATH)
        else:
            error = "Wrong source"
            return render_template("product_display.html", products=[], error=error)
    except FileNotFoundError:
        # Not required by prompt, but helpful
        error = "Data file not found"
        return render_template("product_display.html", products=[], error=error)
    except (json.JSONDecodeError, ValueError):
        error = "Error reading data file"
        return render_template("product_display.html", products=[], error=error)

    # Filter by id if provided
    if id_param is not None:
        if not str(id_param).isdigit():
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)

        wanted_id = int(id_param)
        filtered = [p for p in products_list if p.get("id") == wanted_id]

        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)

        products_list = filtered

    return render_template("product_display.html", products=products_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
