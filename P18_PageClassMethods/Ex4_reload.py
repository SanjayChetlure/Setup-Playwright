import time

from playwright.sync_api import Page, expect


def test_getRefreshThWebpage(page:Page):
    page.goto("https://www.google.com/")
    time.sleep(2)
    page.reload()

    time.sleep(10)
