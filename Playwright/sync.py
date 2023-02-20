#Synchronous Method
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #Uses chromium to launch a new browser
    browser = p.chromium.launch(headless=False)
    #Opens up a new page
    page = browser.new_page()
    #Opens the url
    page.goto("https://the-internet.herokuapp.com/")
    #Takes a screenshot of the page
    page.screenshot(path="demo.png")
    #Closes the browser
    browser.close()