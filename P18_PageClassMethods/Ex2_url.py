import time

from playwright.sync_api import Page, expect


def test_getURLFromBrowser(page:Page):
    page.goto("https://www.google.com/")
    currentURL=page.url
    print(currentURL)

    time.sleep(10)
