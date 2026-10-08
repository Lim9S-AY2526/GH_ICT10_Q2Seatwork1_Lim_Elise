# Working with Lists, Strings, and PyScript Display
from pyscript import display, document

# Lists of countries and their nicknames
countries = [
    "philippines", 
    "thailand", 
    "indonesia", 
    "vietnam", 
    "singapore", 
    "malaysia", 
    "myanmar", 
    "cambodia", 
    "laos", 
    "brunei", 
    "east timor"
]

nicknames = [
    "Pearl of the Orient Seas",
    "Land of Smiles",
    "Emerald of the Equator",
    "The Land of the Ascending Dragon",
    "The Lion City",
    "Truly Asia",
    "The Golden Land",
    "Kingdom of Wonder",
    "Land of a Million Elephants",
    "Abode of Peace",
    "The Rising Sun of Timor"
]


# Function to clean input and look up the nickname in the atlas
def find_atlas_nickname(user_country):
    # Convert input to lowercase
    cleaned_input = user_country.lower()

    # Checking list membership with the "in" operator
    if cleaned_input in countries:
        # Finding the index position in the countries list
        position = countries.index(cleaned_input)
        # Getting the matching nickname using the same index position
        return nicknames[position]
    else:
        return "Country not found in Southeast Asia."


# Function triggers when the user clicks the reveal button
def reveal_country_nickname(e):
    # Clearing previous output from the result div
    document.getElementById("result").innerHTML = ""

    # Getting the text entered in the input box
    user_country = document.getElementById("country_input").value

    # Checking for empty input
    if user_country == "":
        display("Please enter a country name.", target="result")
        return

    # Getting the nickname from our atlas lookup function
    nickname = find_atlas_nickname(user_country)

    # Displaying the result on screen
    if "not found" in nickname:
        display(f"{nickname}", target="result")
    else:
        display(f"Nickname: {nickname}", target="result")