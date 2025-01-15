const fs = require('fs');
const path = require('path');

// Dictionary of countries and their capitals
countryToCapital = {
    "Algeria": "Algiers",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Bahrain": "Manama",
    "Belgium-Luxembourg": "Brussels", 
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
    "Czechoslovakia": "Prague",
    "Denmark": "Copenhagen",
    "East Asia & Pacific": null, 
    "Egypt, Arab Rep.": "Cairo",
    "Europe & Central Asia": null, 
    "Finland": "Helsinki",
    "France": "Paris",
    "Gabon": "Libreville",
    "German Democratic Republic": "East Berlin", 
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
    "Latin America & Caribbean": null, 
    "Malaysia": "Kuala Lumpur",
    "Mexico": "Mexico City",
    "Middle East & North Africa": null, 
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "North America": null, 
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Other Asia, nes": null, 
    "Pakistan": "Islamabad",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Saudi Arabia": "Riyadh",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Solomon Islands": "Honiara",
    "South Africa": "Pretoria", 
    "South Asia": null,  
    "Soviet Union": "Moscow",  
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sub-Saharan Africa": null,  
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Unspecified": null, 
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yugoslavia,FR(Serbia/Montenegr": "Belgrade", 
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}

// Function to replace country names with capitals recursively
function replaceCountryWithCapital(obj) {
    if (typeof obj === 'object' && obj !== null) {
        for (const key in obj) {
            if (typeof obj[key] === 'object') {
                replaceCountryWithCapital(obj[key]);
            } else if (countryToCapital[key]) {
                obj[countryToCapital[key]] = obj[key];
                delete obj[key];
            }
        }
    }
}

// Path to the folder containing JSON files
const folderPath = '../json'; // Update to your folder path

fs.readdir(folderPath, (err, files) => {
    if (err) {
        console.error('Error reading the directory:', err);
        return;
    }

    files.forEach(file => {
        const filePath = path.join(folderPath, file);

        // Only process JSON files
        if (path.extname(file) === '.json') {
            fs.readFile(filePath, 'utf8', (err, data) => {
                if (err) {
                    console.error(`Error reading file ${file}:`, err);
                    return;
                }

                let jsonData;
                try {
                    jsonData = JSON.parse(data);
                } catch (parseErr) {
                    console.error(`Error parsing JSON in file ${file}:`, parseErr);
                    return;
                }

                // Replace country names with capitals
                replaceCountryWithCapital(jsonData);

                // Write the updated JSON back to the file
                fs.writeFile(filePath, JSON.stringify(jsonData, null, 2), (err) => {
                    if (err) {
                        console.error(`Error writing file ${file}:`, err);
                    } else {
                        console.log(`Updated file: ${file}`);
                    }
                });
            });
        }
    });
});
