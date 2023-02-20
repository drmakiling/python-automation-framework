#Asynchronous Method
import asyncio
from playwright.async_api import async_playwright

async def main():
    #Making async_playwright as alias 'p'
    async with async_playwright() as p:
        #Uses chromium to launch a new browser
        browser = await p.chromium.launch(headless=False)
        #Opens up a new page
        page = await browser.new_page()
        #Opens the url
        await page.goto("https://the-internet.herokuapp.com/")
        #Prints the page title
        print(await page.title())
        #Closes the browser
        await browser.close()

    asyncio.run(main())