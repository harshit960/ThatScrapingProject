import os

# Dictionary mapping capitals to country codes
capital_to_country = {
    "Abuja": "NGA",
    "Accra": "GHA",
    "AddisAbaba": "ETH",
    "Algiers": "DZA",
    "Ankara": "TUR",
    "Antananarivo": "MDG",
    "Ashgabat": "TKM",
    "Astana": "KAZ",
    "Asunción": "PRY",
    "Baghdad": "IRQ",
    "Bamako": "MLI",
    "Bangkok": "THA",
    "Bangui": "CAF",
    "Beijing": "CHN",
    "Berlin": "DEU",
    "Bishkek": "KGZ",
    "Bogota": "COL",
    "Bogotá": "COL",
    "Brasília": "BRA",
    "Brazzaville": "COG",
    "Bucharest": "ROM",
    "BuenosAires": "ARG",
    "Cairo": "EGY",
    "Canberra": "AUS",
    "Caracas": "VEN",
    "Conakry": "GIN",
    "Copenhagen": "DNK",
    "Dakar": "SEN",
    "Damascus": "SYR",
    "Dodoma": "TZA",
    "Gaborone": "BWA",
    "Georgetown": "GUY",
    "Hanoi": "VNM",
    "Harare": "ZWE",
    "Helsinki": "FIN",
    "Islamabad": "PAK",
    "Jakarta": "IDN",
    "Kabul": "AFG",
    "Kampala": "UGA",
    "Khartoum": "SDN",
    "Kinshasa": "ZAR",
    "KualaLumpur": "MYS",
    "Kyiv": "UKR",
    "LaPaz": "BOL",
    "Libreville": "GAB",
    "London": "GBR",
    "Luanda": "AGO",
    "Lusaka": "ZMB",
    "Madrid": "ESP",
    "Manila": "PHL",
    "Maputo": "MOZ",
    "MexicoCity": "MEX",
    "Minsk": "BLR",
    "Montevideo": "URY",
    "Moscow": "RUS",
    "Muscat": "OMN",
    "N'Djamena": "TCD",
    "Nairobi": "KEN",
    "Naypyidaw": "MMR",
    "NewDelhi": "IND",
    "Niamey": "NER",
    "Nicosia": "CYP",
    "Nouakchott": "MRT",
    "Nuuk": "GRL",
    "Oslo": "NOR",
    "Ottawa": "CAN",
    "Ouagadougou": "BFA",
    "Paris": "FRA",
    "PortMoresby": "PNG",
    "Pretoria": "ZAF",
    "Quito": "ECU",
    "Rabat": "MAR",
    "Riyadh": "SAU",
    "Rome": "ITA",
    "Sanaa": "YEM",
    "Santiago": "CHL",
    "Stockholm": "SWE",
    "Tashkent": "UZB",
    "Tehran": "IRN",
    "Tokyo": "JPN",
    "Tripoli": "LBY",
    "Tunis": "TUN",
    "Ulaanbaatar": "MNG",
    "WashingtonDC": "USA",
    "Wellington": "NZL",
    "Warsaw": "POL",
    "Yamoussoukro": "CIV",
    "Yaoundé": "CMR"
}

# Invert the dictionary for easier mapping
country_to_capital = {v: k for k, v in capital_to_country.items()}

# Folder path where files are located
folder_path = "newexpjson"

# Rename files
for filename in os.listdir(folder_path):
    # Check if the file name ends with .csv
    if filename.endswith(".json"):
        # Get the country code from the file name
        country_code = filename.split(".")[0]
        # Find the corresponding capital name
        capital_name = country_to_capital.get(country_code)
        if capital_name:
            # Generate the new file name
            new_filename = f"{capital_name}.json"
            # Get full paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Country code {country_code} not found in dictionary.")
