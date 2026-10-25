import time

from playwright.sync_api import Page, expect


def test_goForward(page:Page):
    page.goto("https://www.flipkart.com/")
    time.sleep(2)
    page.goto("https://www.amazon.in/")
    time.sleep(2)
    page.go_back()
    time.sleep(2)
    page.go_forward()

    time.sleep(10)
