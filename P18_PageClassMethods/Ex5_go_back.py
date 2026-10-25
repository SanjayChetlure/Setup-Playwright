import time

from playwright.sync_api import Page, expect


def test_goBack(page:Page):
    page.goto("https://www.flipkart.com/")
    time.sleep(2)
    page.goto("https://www.amazon.in/")
    time.sleep(2)
    page.go_back()

    time.sleep(10)
