import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver with options (no headless for visibility)
options = Options()
options.headless = False  # Set to True if you don't want the browser window to open
driver = webdriver.Chrome(options=options)


def scrape_data(country, year, product_code):
    url = f"https://wits.worldbank.org//CountryProfile/en/Country/{country}/Year/{year}/TradeFlow/Export/Partner/ALL/Product/{product_code}"

    # Open the URL
    driver.get(url)

    # Wait for the page to load (this is to ensure the JavaScript variables are available)
    # time.sleep(5)  # Adding a delay to ensure the page loads completely

    # Extract 'partnerChartData' JavaScript variable from the page
    partner_data = driver.execute_script("return window.partnerChartData")

    # Extract '01_05_Animal' JavaScript variable from the page

    return partner_data

def generate_years(start, end):
    # Generate the list of years from start to end (inclusive)
    return [str(year) for year in range(start, end + 1)]

categories = {
    "01-05_Animal": "Animals & Animal Products",
    "06-15_Vegetable": "Vegetable Products",
    "16-24_FoodProd": "Prepared Foodstuffs; Beverages, Spirits, Vinegar, Tobacco and Manufactured Tobacco Substitutes",
    "25-26_Minerals": "Mineral Products",
    "28-38_Chemicals": "Products of the Chemical or Allied Industries",
    "39-40_PlastiRub": "Plastics and Articles thereof; Rubber and Articles thereof",
    "41-43_HidesSkin": "Raw Hides and Skins, Leather, Furskins, and Articles thereof; Saddlery and Harness; Travel Goods, Handbags, and Similar Containers; Articles of Animal Gut (Other than Silk-worm Gut)",
    "44-49_Wood": "Wood and Articles of Wood; Wood Charcoal; Cork and Articles of Cork; Manufactures of Straw, of Esparto or of Other Plaiting Materials; Basketware and Wickerwork",
    "50-63_TextCloth": "Textiles and Textile Articles",
    "64-67_Footwear": "Footwear, Headgear, Umbrellas, Sun Umbrellas, Walking-sticks, Seat-sticks, Whips, Riding-crops, and Parts thereof; Prepared Feathers and Articles Made therewith; Artificial Flowers; Articles of Human Hair",
    "68-71_StoneGlas": "Articles of Stone, Plaster, Cement, Asbestos, Mica or Similar Materials; Ceramic Products; Glass and Glassware",
    "OresMtls": "Natural or Cultured Pearls, Precious or Semi-precious Stones, Precious Metals, Metals Clad with Precious Metal, and Articles thereof; Imitation Jewellery; Coin",
    "72-83_Metals": "Base Metals and Articles of Base Metal",
    "84-85_MachElec": "Machinery and Mechanical Appliances; Electrical Equipment; Parts thereof; Sound Recorders and Reproducers, Television Image and Sound Recorders and Reproducers, and Parts and Accessories of such Articles",
    "86-89_Transport": "Vehicles, Aircraft, Vessels, and Associated Transport Equipment",
    "manuf": "Optical, Photographic, Cinematographic, Measuring, Checking, Precision, Medical or Surgical Instruments and Apparatus; Clocks and Watches; Musical Instruments; Parts and Accessories thereof",
    "90-99_Miscellan": "Miscellaneous Manufactured Articles",
}
product_code = [
    "01-05_Animal",
    "06-15_Vegetable",
    "16-24_FoodProd",
    "25-26_Minerals",
    "28-38_Chemicals",
    "39-40_PlastiRub",
    "41-43_HidesSkin",
    "44-49_Wood",
    "50-63_TextCloth",
    "64-67_Footwear",
    "68-71_StoneGlas",
    "OresMtls",
    "72-83_Metals",
    "84-85_MachElec",
    "86-89_Transport",
    "manuf",
    "90-99_Miscellan"
]

country = ["CAN"]
year = generate_years(1989, 2022)

def export_to_csv(partner_data, year, product_code):
    # Open a CSV file to append data
    with open(country[0]+".csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([year, product_code, partner_data])


for i in range(len(year)):
    for j in range(len(product_code)):
        partner_data = scrape_data(country[0], year[i], product_code[j])
        print(year[i], categories[product_code[j]], partner_data, "/n")
        export_to_csv(partner_data, year[i], categories[product_code[j]])


# Close the WebDriver
driver.quit()
