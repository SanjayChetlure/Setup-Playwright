import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators6_get_by_place(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    time.sleep(2)

    # page.get_by_title("Home page link")  -> this will return text
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    expect(page.get_by_title("Tooltip text")).to_have_text("This text has a tooltip")
    time.sleep(5)



