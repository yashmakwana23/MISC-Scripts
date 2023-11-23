urls=["https://play.google.com/store/search?q=Aristocrat Leisure","https://play.google.com/store/search?q=Konami Digital Entertainment"]

import requests
from bs4 import BeautifulSoup
from lxml import html

def get_links_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def find_url_with_keyword(links, keyword):
    z=0
    for link in links:
        # print(link)
        if keyword in link:
            z=z+1
            if z==3: #update according to link you want
                return link

def get_xpath_result(url, xpath):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    result = tree.xpath(xpath)
    return result

# Step 1: Get all links from link1
for url in urls:
    link1 = url
    urlkey = "/store/apps/details?id="
    links = get_links_from_url(link1)

    # Step 2: Find the first link with the keyword
    result = find_url_with_keyword(links, urlkey)

    # Step 3: Generate the final URL
    final_url = f"https://play.google.com{result}"

    # Step 4: Use the final URL to get XPath results
    xpath = """//*[@id="developer-contacts"]/div/div[2]/div/a/div/div[2]"""  # Replace with the XPath you want to use
    results = get_xpath_result(final_url, xpath)

    # Step 5: Print the results
    if results:
        for result in results:
            print(result.text_content())
    else:
        print("XPath not found.")