from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page):
    page.goto("https://www.google.com/")      #bydefauly - Chromium browser will be launched
    expect(page).to_have_url("https://www.google.com/")

    # expect is function in which we need to pass page fixture for validation


def test_verifyTitle(page:Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_title("Google")


def test_getPageUrlTitle(page:Page):
    page.goto("https://www.google.com/")
    urlValue=page.url
    titleValue=page.title()
    print("page url is : "+urlValue)
    print("page title is : "+titleValue)

