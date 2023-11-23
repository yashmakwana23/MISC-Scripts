from googleapiclient.discovery import build
from time import sleep
def google_custom_search(api_key, cse_id, query, num_results=10):
    service = build("customsearch", "v1", developerKey=api_key)
    results = []

    while len(results) < num_results:
        response = service.cse().list(q=query, cx=cse_id, num=min(10, num_results - len(results)), start=len(results) + 1).execute()
        results.extend(response.get('items', []))

        if 'nextPage' not in response['queries']:
            break

    return results

# Example Usage:
api_key = ''
cse_id = ''
query = 'Clash of Clans Topup'
lista=["SimCity  Top up","BATTLEFIELD 2042 Top up"]
for gamename in lista:
    results = google_custom_search(api_key, cse_id, gamename, num_results=100)
    print(gamename)
    # Print all links
    sleep(5)
    for i, item in enumerate(results, start=1):
        print(f"{gamename}: {item['link']}")
