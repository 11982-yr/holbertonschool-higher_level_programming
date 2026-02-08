from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    # Build an absolute path so it works no matter where you run it from
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "items.json")

    items_list = []
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            items_list = data.get("items", [])
            if not isinstance(items_list, list):
                items_list = []
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template("items.html", items=items_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
