import time

from playwright.sync_api import Page, expect


def test_close(page:Page):
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(2000)
    time.sleep(10)
