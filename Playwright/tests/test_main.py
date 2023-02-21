#from page_objects import InternetPage
from playwright.sync_api import Page, expect
import pytest

# Verify the file is downloaded and it exists on the machine
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
    print(download.path())
    download.save_as("/home/dmakiling-admin/automation-framework-development/upload-me.txt")

# Verify the file is uploaded
def test_file_upload(page: Page):
    # Navigate to https://the-internet.herokuapp.com/
    page.goto("https://the-internet.herokuapp.com/")

    # Click File Upload Link
    page.get_by_role("link", name="File Upload").click()

    # Upload file from previous test case
    page.locator("#file-upload").click()
    page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("/home/dmakiling-admin/automation-framework-development/upload-me.txt")
    page.get_by_role("button", name="Upload").click()

    # Verify the file is uploaded
    assert page.inner_text('h3') == "File Uploaded!"

#Verify User is logged in
def test_login(page: Page):
    # Navigate to https://the-internet.herokuapp.com/
    page.goto("https://the-internet.herokuapp.com/")

    # Click Basic Auth link
    page.get_by_role("link", name="Basic Auth").click()

    # Enter in the credentials
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("admin")
    page.get_by_role("button", name="Sign in").click()
    page.goto("http://the-internet.herokuapp.com/basic_auth")

    # Verify User is logged in
    assert page.inner_text('p') == "Congratulations! You must have the proper credentials."

# Verify New Window is opened
def test_new_window(page: Page):
    # Navigate to https://the-internet.herokuapp.com/
    page.goto("https://the-internet.herokuapp.com/")

    # Click Multiple Windows link
    page.get_by_role("link", name="Multiple Windows").click()

    # Click In "Click Here"
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Click Here").click()
    page1 = page1_info.value

    # Verify the text in the New Window "New Window" 
    assert page1.title() == "New Window"