#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = []

            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, PermissionError, csv.Error):
        return False
