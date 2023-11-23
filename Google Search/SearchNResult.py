import requests
from bs4 import BeautifulSoup

def search_and_get_first_result(keyword):
    url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    first_result_element = soup.find('a', {'class': 'BVG0Nb'})
    
    if first_result_element is not None:
        first_result = first_result_element['href']
        return first_result
    else:
        return None


# Example usage:
KeyW="Activision Blizzard"
search_keyword = f"{KeyW} Google Play Store"
first_result = search_and_get_first_result(search_keyword)

if first_result is not None:
    print(f"The first result for '{search_keyword}' is:")
    print(first_result)
else:
    print(f"No result found for '{search_keyword}'.")
