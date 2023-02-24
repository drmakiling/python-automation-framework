from playwright.sync_api import expect, Playwright
import pytest

# # Verify the file is downloaded and it exists on the machine
# def test_file_download(playwright: Playwright) -> None:
#     # Navigate to https://the-internet.herokuapp.com/
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://the-internet.herokuapp.com/")

#     # Click File Download Link
#     page.get_by_role("link", name="File Download", exact=True).click()

#     # Select one of the files ("upload-me.txt")
#     with page.expect_download() as download_info:
#         page.get_by_role("link", name="PIHU.png").click()

#     # Verify the file is downloaded and it exists on the machine    
#     download = download_info.value
#     print(download.path())
#     download.save_as("/home/dmakiling-admin/automation-framework-development/PIHU.png")
#     browser.close()

# # Verify the file is uploaded
# def test_file_upload(playwright: Playwright):
#     # Navigate to https://the-internet.herokuapp.com/
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://the-internet.herokuapp.com/")

#     # Click File Upload Link
#     page.get_by_role("link", name="File Upload").click()

#     # Upload file from previous test case
#     page.locator("#file-upload").click()
#     page.locator("#file-upload").click()
#     page.locator("#file-upload").set_input_files("/home/dmakiling-admin/automation-framework-development/PIHU.png")
#     page.get_by_role("button", name="Upload").click()

#     # Verify the file is uploaded
#     assert page.inner_text('h3') == "File Uploaded!"

def test_login(playwright: Playwright) -> None:
        # Navigate to https://the-internet.herokuapp.com/
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        # Click Basic Auth link
        page.get_by_role("link", name="Basic Auth").click()

        # Enter in the credentials
        context = browser.new_context(http_credentials={'username':'admin', 'password':'admin'})
        page = context.new_page()
        page.goto("http://the-internet.herokuapp.com/basic_auth")

        # Locate <p> in page
        result = page.locator("#content p")

        # Finds the correct text
        expect(result).to_have_text('Congratulations! You must have the proper credentials.')

        # Close browser
        context.close()
        browser.close()

# # Verify New Window is opened
# def test_new_window(playwright: Playwright):
#     # Navigate to https://the-internet.herokuapp.com/
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto("https://the-internet.herokuapp.com/")

#     # Click Multiple Windows link
#     page.get_by_role("link", name="Multiple Windows").click()

#     # Click In "Click Here"
#     with page.expect_popup() as page1_info:
#         page.get_by_role("link", name="Click Here").click()
#     page1 = page1_info.value

#     # Verify the text in the New Window "New Window" 
#     assert page1.title() == "New Window"