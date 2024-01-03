"""
Goal: Generate a json file of countries and their 2020 data of HDI
Read from copy and pasted 2022 data
Write json format of Country name, cut out parts with parenthesis
Subtract value after HDI from HDi value to get 2020 info
"""
import json
country_to_hdi = {}
with open("2022_hdr_data.txt", "r", encoding="utf-8") as fin: raw_data = iter(fin.readlines())
current_line, current_country = next(raw_data), None
while True:
    try:
        current_line = next(raw_data)
    except:
        break
    if current_line[0].isalpha() and current_line[0].isupper():
        current_country = current_line.strip() if "(" not in current_line \
            else current_line[:current_line.find("(")].strip()
        country_to_hdi[current_country] = float(next(raw_data))
        country_to_hdi[current_country] -= float(next(raw_data))
        country_to_hdi[current_country] = round(country_to_hdi[current_country], 3)
with open("data/hdi.json", "w", encoding="utf-8") as fout:
    fout.write(json.dumps(country_to_hdi, indent=1))


# A country IF: first letter isalpha and isupper
# Remove after parenthesis and strip it
# Make that the current key
# Add next line and subtract next line
# Keep iterating until the country condition is met