import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators4_get_by_label(page:Page):

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    time.sleep(50)

    # fill is method like sendkeys in selenium
    #Enter FN
    page.get_by_label("First name:").fill("abc")

    #Enter LN
    page.get_by_label("Last name:").fill("xyz")

    # Enter Email
    page.get_by_label("Email:").fill("abc@123")

    time.sleep(5)



