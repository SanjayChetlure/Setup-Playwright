import re
import time

import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
    for i in range(5):
        button=page.get_by_role("button",name=re.compile("ST.*"))
        button.click()
        page.wait_for_timeout(2000)

