import csv
import json
from collections import defaultdict
import re
import os
import time
# Initialize the data structure

# Read the CSV file
count = 0
success = 0
folder_path = "expout"
# print(os.listdir(folder_path))
for file_name in os.listdir(folder_path):
# for file_name in ['Abuja.csv', 'Accra.csv', 'AddisAbaba.csv', 'Algiers.csv', 'Ankara.csv', 'Antananarivo.csv', 'Ashgabat.csv', 'Astana.csv', 'Asunción.csv', 'Baghdad.csv', 'Bamako.csv', 'Bangkok.csv', 'Bangui.csv', 'Beijing.csv', 'Berlin.csv', 'Bishkek.csv', 'Bogota.csv', 'Bogotá.csv', 'Brasília.csv', 'Brazzaville.csv', 'Bucharest.csv', 'BuenosAires.csv', 'Cairo.csv', 'Canberra.csv', 'Caracas.csv', 'Conakry.csv', 'Copenhagen.csv', 'Dakar.csv', 'Damascus.csv', 'Dodoma.csv', 'Gaborone.csv', 'Georgetown.csv', 'Hanoi.csv', 'Harare.csv', 'Helsinki.csv', 'Islamabad.csv', 'Jakarta.csv', 'Kabul.csv', 'Kampala.csv', 'Khartoum.csv', 'Kinshasa.csv', 'KualaLumpur.csv', 'Kyiv.csv', 'LaPaz.csv', 'Libreville.csv', 'London.csv', 'Luanda.csv', 'Lusaka.csv', 'Madrid.csv', 'Manila.csv', 'Maputo.csv', 'MexicoCity.csv', 'Minsk.csv', 'Montevideo.csv', 'Moscow.csv', 'Muscat.csv', "N'Djamena.csv", 'Nairobi.csv', 'NAM.csv', 'Naypyidaw.csv', 'NewDelhi.csv', 'Niamey.csv', 'Nicosia.csv', 'Nouakchott.csv', 'Nuuk.csv', 'Oslo.csv', 'Ottawa.csv', 'Ouagadougou.csv', 'Paris.csv', 'POL.csv', 'PortMoresby.csv', 'Pretoria.csv', 'Quito.csv', 'Rabat.csv', 'Riyadh.csv', 'Rome.csv', 'Sanaa.csv', 'Santiago.csv', 'Stockholm.csv', 'Tashkent.csv', 'Tehran.csv', 'testtt.csv', 'Tokyo.csv', 'Tripoli.csv', 'Tunis.csv', 'Ulaanbaatar.csv', 'WashingtonDC.csv', 'Wellington.csv', 'Yamoussoukro.csv', 'Yaoundé.csv']:
    data = {"Main Partners": defaultdict(lambda: {"Imports": defaultdict(dict)})}
    print(file_name)
    with open("expout/" + file_name, mode="r",encoding='latin-1') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                try:
                    year, category, partners_data = row
                    # print(f"Processing row: {row}")  # Debug log for the row
                except Exception as e:
                    print(f"Error processing row: {row}")
                    print(f"Row-level error: {e}")
                    continue         

                partners_data = eval(
                    partners_data
                )  # Convert string representation of list to actual list
                # Process each partner's data
                for partner in partners_data:
                    label = partner["label"]
                    if "data" in partner:
                        description = partner["data"][
                            "description"
                        ]  # Extract description
                        share_match = re.search(
                            r"Share\(%\):\s*([\d\.]+)", description
                        )  # Regex to find Share(%)

                        if share_match:
                            share_percentage = share_match.group(
                                1
                            )  # Extract the Share(%) value
                            if "Others" not in label:
                                if "Others" in label:
                                    label = "Others (" + label.split("(")[-1]
                                data["Main Partners"][year]["Imports"][category][
                                    label
                                ] = f"{float(share_percentage):.2f}"
                success += 1
                print("success:", success)


            except Exception as e:
                count += 1
                print(f"error: ", count,e)
                continue

    # Convert defaultdict to dict
    data["Main Partners"] = dict(data["Main Partners"])
    for year in data["Main Partners"]:
        data["Main Partners"][year]["Imports"] = dict(
            data["Main Partners"][year]["Imports"]
        )

    output_json_file = (
        "expjson/" + file_name.replace(".csv", ".json")
    )  # Use the same directory and name as the CSV file
    with open(output_json_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(count)
    time.sleep(0.1) 