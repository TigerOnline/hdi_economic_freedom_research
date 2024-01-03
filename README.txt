Steps to run this:
1. Copy and paste HDI data from https://hdr.undp.org/data-center/country-insights#/ranks into 2022_hdr_data.txt
2. Run the hdi_json_create.py
3. Copy and paste the 2019 Economic Freedom of the World Index from https://en.wikipedia.org/wiki/List_of_sovereign_states_by_economic_freedom into 2019_economic_freedom_data
4. Run the economic_freedom_index_json_create.py
5. Run data_cleaner.py to compare what's missing
6. See the list of missing countries. Go through the list.
7. If the country name is too specific in the hdi.json, then correct the name in 2022_hdr_data.txt
8. If the country name is too specific in the economic_index.json, then correct the name in 2019_economic_freedom_data.txt
9. If the country doesn't exist in economic_index.json, find the country in https://www.fraserinstitute.org/economic-freedom/map?geozone=world&page=map&year=2020
10. Fill in the 2019_economic_freedom_data at the bottom with the economic indices, make sure it is in the same format as above
11. If the country doesn't exist on fraserinstitute, HDI of these missing countries will be displayed in a separate category later
12. Rerun economic_freedom_index_json_create.py and hdi_json_create.py