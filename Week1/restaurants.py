# Tui Popenoe
# restaurants.py



# dict of {str:int}
name_to_rating = {
    'Georgie Progie' : 87,
    'Queen St. Cafe' : 82,
    'Dumplings R Us' : 71,
    'Mexicans Grill' : 85,
    'Deep Fried All' : 52
}

# dict of {str: list of str}
price_to_name = {
    '$' : ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried All'],
    '$$' : ['Mexicans Grill'],
    '$$$' : ['Georgie Porgie'],
    '$$$$' : []
}

# dict of {str:list of str}

type_to_name = {
    'Canadian' : ['Georgie Porgie'],
    'Pub Food' :  ['Georgie Porgie', 'Deep Fried All'],
    'Malaysian' : ['Queen St. Cafe'],
    'Thai' : ['Queen St. Cafe'],
    'Chinese' : ['Dumplings R Us'],
    'Mexican' : ['Mexicans Grill']
}

FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str]

    Find restaurants