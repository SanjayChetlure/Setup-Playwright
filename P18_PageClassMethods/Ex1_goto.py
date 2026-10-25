import time

from playwright.sync_api import Page, expect


def test_OpenApp(page:Page):
    page.goto("https://www.google.com/")
    time.sleep(10)
