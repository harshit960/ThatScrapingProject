import csv
import json
from collections import defaultdict
import re

# Initialize the data structure
data = {
    "Main Partners": defaultdict(lambda: {"Imports": defaultdict(dict)})
}

# Read the CSV file
with open('output/ZAF.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        year, category, partners_data = row
        try:
            partners_data = eval(partners_data)  # Convert string representation of list to actual list
            # Process each partner's data
            for partner in partners_data:
                label = partner['label']
                if 'data' in partner:
                    description = partner['data']['description']  # Extract description
                    share_match = re.search(r'Share\(%\):\s*([\d\.]+)', description)  # Regex to find Share(%)

                    if share_match:
                        share_percentage = share_match.group(1)  # Extract the Share(%) value
                        if 'Others' not in label:
                            if 'Others' in label:
                                label = 'Others (' + label.split('(')[-1]
                            data["Main Partners"][year]["Imports"][category][label] = f"{float(share_percentage):.2f}"
        except Exception as e:
            print(f"processing row")
            continue

# Convert defaultdict to dict
data["Main Partners"] = dict(data["Main Partners"])
for year in data["Main Partners"]:
    data["Main Partners"][year]["Imports"] = dict(data["Main Partners"][year]["Imports"])

output_json_file = 'bangui.json'  # Use the same directory and name as the CSV file
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)