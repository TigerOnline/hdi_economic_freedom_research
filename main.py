"""
List the HDIs of each 10% HDI range, from 0.3 to 1
Get an average economic freedom index of each HDI range, and the # of countries in that range

List the Economic freedom of each 10% Economic freedom range, from 0 to 100
Get an average HDI of each economic freedom range, and the # of countries in that range
Dictionary with keys as each range. The value is a dictionary {country:economic freedom}
"""
import json, math
with open("data/economic_index.json", "r", encoding="utf-8") as fin:
    country_to_freedom_index = json.loads(fin.read())
with open("data/hdi.json", "r", encoding="utf-8") as fin:
    country_to_hdi = json.loads(fin.read())

# range number is lower bound
hdi_deciles = {hdi_lower_bound:{} for hdi_lower_bound in [round(i*0.1, 1) for i in range(3, 10)]}

# if you use fromkeys, the empty dictionary isn't a copy. It's a direct reference to the same dict
hdi_deciles["unranked"] = {}
freedom_deciles = {freedom_lower:{} for freedom_lower in [i*10 for i in range(0, 10)]}
freedom_deciles["unranked"] = {}

# getting the hdi decile
for country in country_to_hdi:
    hdi_value = country_to_hdi[country]
    lower_bound = math.floor(hdi_value*10)/10
    # print(country, hdi_value, lower_bound)
    hdi_deciles[lower_bound][f"{country}"] = [hdi_value, country_to_freedom_index[country]]\
    if country in country_to_freedom_index \
        else [hdi_value, "NA"]

for country in country_to_freedom_index:
    freedom_index = country_to_freedom_index[country]
    lower_bound = hdi_value//10 * 10
    # print(country, hdi_value, lower_bound)
    freedom_deciles[lower_bound][f"{country}"] = [freedom_index, country_to_hdi[country]] if country in country_to_hdi \
        else [freedom_index, "NA"]

for lower_bound in hdi_deciles:
    valid_scores = [i[1] for i in hdi_deciles[lower_bound].values() if i[1]!="NA"]
    total_hdi_score = sum(valid_scores)
    total_countries = len(valid_scores)
    hdi_deciles[lower_bound]["Average"] = ["", total_hdi_score/total_countries] if total_countries else ["", 0]
    #  Staying consistent with the format of the other columns

with open("finished_product/hdi_deciles.csv", "w", encoding="utf-8") as fout:
    fout.write("HDI Bracket,HDI Value,Economic Freedom Index\n\n")
    for lower_bound in hdi_deciles:
        if lower_bound != "unranked":
            fout.write(f"{lower_bound}-{round(float(lower_bound)+0.1, 1)} HDI\n")
        else:
            fout.write("No HDI Data")
        for country in hdi_deciles[lower_bound]:
            country_hdi_and_freedom = hdi_deciles[lower_bound][country]
            if country == "Average":
                fout.write(f"Average,,{country_hdi_and_freedom[1]}\n")
                break
            fout.write(f"{country}, {country_hdi_and_freedom[0]}, {country_hdi_and_freedom[1]}\n")
        fout.write("\n\n")
