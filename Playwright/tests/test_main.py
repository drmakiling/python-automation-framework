from playwright.sync_api import Page, expect
import pytest

#def test_title(page: Page):
    #page.goto("https://the-internet.herokuapp.com/")
    #assert page.inner_text('h1') == "Welcome to the-internet"

def test_file_download(page: Page):
    # Navigate to https://the-internet.herokuapp.com/
    page.goto("https://the-internet.herokuapp.com/")

    # Click File Download Link
    page.get_by_role("link", name="File Download", exact=True).click()

    # Select one of the files ("upload-me.txt")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="upload-me.txt").click()

    # Verify the file is downloaded and it exists on the machine    
    download = download_info.value
    page.wait_for_event(download_info)
    download.path()

#def test_auth(page: Page):
    #page.goto("https://the-internet.herokuapp.com/")
    #page.goto("https://the-internet.herokuapp.com/basic_auth")
    