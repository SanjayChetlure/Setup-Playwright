import time

from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators_get_by_alt_text(page:Page):
    # locate an element, usually image, by its text alternative.  (locate image/logo)
    # If Image element is having attr alt then we can use this locator to locate the image element
    # get_by_alt_text() method return Locator object (like WebElement in selenium)

    #run script on headed mode from UI-right click on python file -> Modify run configuration ->
    # Additional Argument -> --headed --browser=chromium -> Apply -> Save
    # Next when we run script it will run using above config


    page.goto("https://www.flipkart.com/")

    #Apr1:
    # logo = page.get_by_alt_text("Image")       #single matching
    logo=page.get_by_alt_text("Image").nth(0)   #get first image element  -> As this method will fail, when multiple image elements are present on page with same alt text
    expect(logo).to_be_visible()

    #To run script slow
    time.sleep(2)                 #time in sec
    page.wait_for_timeout(2000)   #time in mili sec

    #Apr2:-
    # expect(page.get_by_alt_text("nopCommerce demo store")).to_be_visible()



