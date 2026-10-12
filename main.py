# Working with Parallel Lists without Conditional Statements
from pyscript import display, document

# Parallel lists of countries and nicknames
countries = [
    "cambodia",
    "laos",
    "myanmar (burma)",
    "thailand",
    "vietnam",
    "brunei",
    "indonesia",
    "malaysia",
    "philippines",
    "singapore",
    "timor-leste (east timor)"
]

nicknames = [
    "The Kingdom of Wonder",
    "Land of a Million Elephants",
    "Golden Land",
    "Land of Smiles",
    "Land of the Ascending Dragon",
    "Abode of Peace",
    "Emerald of the Equator",
    "Truly Asia",
    "Pearl of the Orient Seas",
    "Lion City",
    "Land of the Rising Sun"
]


# Function triggered when the button is clicked
def reveal_nickname(e):
    # Clear previous output
    document.getElementById("display1").innerHTML = ""

    # Get country name from dropdown and convert to lowercase
    selected_country = document.getElementById("select_country").value.lower()

    # Get index position directly from the countries list
    index_position = countries.index(selected_country)

    # Fetch matching nickname using the index position
    nickname = nicknames[index_position]

    # Display the result
    display(f"Nickname: {nickname}", target="display1")