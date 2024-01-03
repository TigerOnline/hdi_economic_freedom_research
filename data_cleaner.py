"""
Find what country is in hdi list but not in economic freedom
Find what's in the economic freedom but not in hdi

Later we are categorizing countries in terms of hdi, and listing the economic freedom next to the countries of that hdi
Print the countries that HAS an index but NO HDI, and for the other group
Then manually edit the titles of the 2019 economic freedom list
"""
import json
with open("data/economic_index.json", "r", encoding="utf-8") as fin:
    economic_index = json.loads(fin.read())
with open("data/hdi.json", "r", encoding="utf-8") as fin:
    hdi = json.loads(fin.read())

print("Doesn't exist in economic_freedom_index".center(100, "-"))
for country in hdi:
    if country not in economic_index: print(country)

print("Doesn't exist in economic_freedom_index".center(100, "-"))
for country in economic_index:
    if country not in hdi: print(country)