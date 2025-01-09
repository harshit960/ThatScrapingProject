
# Dictionary mapping country names to capitals
country_to_capital = {
    "Algeria": "Algiers",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Bahrain": "Manama",
    "Belgium-Luxembourg": "Brussels",  # Luxembourg is included
    "Belize": "Belmopan",
    "Brazil": "Brasília",
    "Bulgaria": "Sofia",
    "Cameroon": "Yaoundé",
    "Canada": "Ottawa",
    "Chile": "Santiago",
    "China": "Beijing",
    "Congo, Dem. Rep.": "Kinshasa",
    "Congo, Rep.": "Brazzaville",
    "Cote d'Ivoire": "Yamoussoukro",
    "Cyprus": "Nicosia",
    "Czechoslovakia": "Prague",  # Former country; now Czechia & Slovakia
    "Denmark": "Copenhagen",
    "East Asia & Pacific": None,  # Region, not a country
    "Egypt, Arab Rep.": "Cairo",
    "Europe & Central Asia": None,  # Region, not a country
    "Finland": "Helsinki",
    "France": "Paris",
    "Gabon": "Libreville",
    "German Democratic Republic": "East Berlin",  # Historical
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Greece": "Athens",
    "Hong Kong, China": "Hong Kong",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
    "Korea, Dem. Rep.": "Pyongyang",
    "Korea, Rep.": "Seoul",
    "Kuwait": "Kuwait City",
    "Lao PDR": "Vientiane",
    "Latin America & Caribbean": None,  # Region, not a country
    "Malaysia": "Kuala Lumpur",
    "Mexico": "Mexico City",
    "Middle East & North Africa": None,  # Region, not a country
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "North America": None,  # Region, not a country
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Other Asia, nes": None,  # Undefined or unspecified
    "Pakistan": "Islamabad",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Saudi Arabia": "Riyadh",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Solomon Islands": "Honiara",
    "South Africa": "Pretoria",  # Administrative capital
    "South Asia": None,  # Region, not a country
    "Soviet Union": "Moscow",  # Historical
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sub-Saharan Africa": None,  # Region, not a country
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Unspecified": None,  # Undefined or unspecified
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yugoslavia,FR(Serbia/Montenegr": "Belgrade",  # Historical
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}

import os
import json

# Function to replace country names with capitals (non-recursive)
def replace_countries(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                replace_countries(value)  # Check if value is a dictionary or list
            elif isinstance(value, str) and value in country_to_capital:
                data[key] = country_to_capital[value]  # Replace the country name with capital
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, dict) or isinstance(item, list):
                replace_countries(item)
            elif isinstance(item, str) and item in country_to_capital:
                data[index] = country_to_capital[item]

# Path to folder containing JSON files
folder_path = "newexpjson"  # Change this to your folder path

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        
        # Open and load the JSON file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # Replace countries with capitals
        replace_countries(data)

        # Save the updated JSON back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

print("Replacement completed for all JSON files in the folder.")
