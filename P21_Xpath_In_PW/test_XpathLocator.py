import time

import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
    page.locator("//input[@id='name']").fill("abcd")
    time.sleep(5)