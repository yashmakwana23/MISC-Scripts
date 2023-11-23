import requests
from lxml import html

def extract_content_with_xpath(url, xpath):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        parsed_content = html.fromstring(content)
        elements = parsed_content.xpath(xpath)
        return [element.text_content() for element in elements]
    else:
        print(f"Error fetching content from {url}. Status code: {response.status_code}")
        return None

def main():
    urls=['links']
    xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/c-wiz[6]/div/section/header'  # Replace with your XPath

    for url in urls:
        result = extract_content_with_xpath(url, xpath)
        if result is not None:
            print(result)
        else:
            print(f"Extraction failed for {url}.")

if __name__ == '__main__':
    main()
