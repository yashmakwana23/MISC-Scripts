from googlesearch import search

# List of game names
# game_names = ["2K22","8 Ball Pool","Ace racer","Alchemy Stars","Angel Squad","Apex Legends","Arena breakout"]
game_names=['YouTube']
def get_first_result_link(game_name):
    try:
        # Formulate the search query with game name and "store"
        query = f"{game_name}"
        
        # Perform a Google search for the query
        search_results = search(query,num_results=1)
        
        # Get the first search result URL
        first_result_url = next(search_results)
        
        return first_result_url
    except Exception as e:
        return str(e)

# Iterate through the list of game names and get the first result link
for game_name in game_names:
    result_link = get_first_result_link(game_name)
    print(f"{game_name} : {result_link}\n")
