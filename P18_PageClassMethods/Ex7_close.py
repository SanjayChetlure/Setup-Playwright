import time

from playwright.sync_api import Page, expect


def test_close(page:Page):
    page.goto("https://www.flipkart.com/")
    time.sleep(2)
    page.close()

    time.sleep(10)
