import time

from playwright.sync_api import Page, expect


def test_getTitleOfApp(page:Page):
    page.goto("https://www.google.com/")
    pageTitle=page.title()
    print(pageTitle)

    time.sleep(10)
