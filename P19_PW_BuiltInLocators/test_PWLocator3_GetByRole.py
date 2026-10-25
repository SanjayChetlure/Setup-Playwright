import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators3_get_by_Role(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(5)

    expect(page.get_by_role("heading",name="Automation Testing Practice")).to_be_visible()



