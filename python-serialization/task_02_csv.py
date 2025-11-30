import csv
import json


def convert_csv_to_json(csv_file):
   try:
    data = []
    with open(csv_file, "r", encoding="utf-8") as csvf:
        csv_read = csv.DictReader(csvf)
        for i in csv_read:
            data.append(i)
    with open("data.json", "w", encoding="utf-8") as jsonf:
        json.dump(data, jsonf)
   except FileNotFoundError:
      return False
   else:
      return True
