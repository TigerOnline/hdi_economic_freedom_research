"""
Create a json of all countries and their score from 2019
We're comparing 2019 economic freedom to 2020 since that's the ebst data we can get
"""

import json
with open("2019_economic_freedom_data.txt", "r", encoding="utf-8") as fin:
    country_to_index = {line.split("\t")[1].strip():float(line.split("\t")[2]) for line in fin.readlines()}
with open("data/economic_index.json", "w", encoding="utf-8") as fout:
    fout.write(json.dumps(country_to_index, indent=1))