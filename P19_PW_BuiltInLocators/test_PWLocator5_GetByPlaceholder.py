import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators5_get_by_placeholder(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    # fill is method like sendkeys in selenium
    #Enter FN
    page.get_by_placeholder("Enter Name").fill("abc")

    #Enter LN
    page.get_by_placeholder("Enter EMail").fill("xyz")

    # Enter Email
    page.get_by_placeholder("Enter Phone").fill("1111111111")

    time.sleep(5)



