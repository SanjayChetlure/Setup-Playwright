import time

import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    # page.locator("input#small-searchterms").fill("abc")
    # page.locator("#small-searchterms").fill("abc")

    #tag class
    # page.locator("input.search-box-text.ui-autocomplete-input").fill("abcd")
    # page.locator(".search-box-text.ui-autocomplete-input").fill("abcd")

    #tag attribute
    # page.locator("input[name='q']").fill("abcd")
    # page.locator("[name='q']").fill("abcd")

    #tag class attribute
    page.locator("input.search-box-text.ui-autocomplete-input[name='q']").fill("abcd")
    page.locator(".search-box-text.ui-autocomplete-input[name='q']").fill("abcd")

    time.sleep(5)