import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators7_get_by_testId(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    time.sleep(2)

    # page.get_by_title("Home page link")  -> this will return text
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    time.sleep(5)



