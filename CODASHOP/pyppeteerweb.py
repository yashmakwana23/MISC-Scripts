urls = [
"https://www.codashop.com/en-sg/ludo-club","https://www.codashop.com/th-th/ludo-club"]
import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError, ElementHandleError


async def extract_content_with_xpath(page, url, xpath):
    try:
        await page.goto(url)
        await page.waitForXPath(xpath, options={"timeout": 60000, "visible": True})  # Increased timeout to 60 seconds
        elements = await page.xpath(xpath)
        content = await page.evaluate('(element) => element.textContent', elements[0])
        return content
    except TimeoutError:
        print(f"{url}")
        return None
    except ElementHandleError:
        print(f"{url}")
        return None
    except Exception as e:
        print(f"{url}: {e}")
        return None

async def main():
    global b
    b=1
    browser = await launch(headless=False)
    page = await browser.newPage()


    xpath = '//*[@id="voucher"]/ul'  # Replace with your XPath

    for url in urls:
        result = await extract_content_with_xpath(page, url, xpath)
        if result is not None:
            print(f"{b}. {result}")
            b=b+1

    await browser.close()

# Run the asyncio loop
asyncio.get_event_loop().run_until_complete(main())
