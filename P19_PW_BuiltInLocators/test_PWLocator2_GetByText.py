import time,re
from playwright.sync_api import Page, expect     #except for verification


def test_verify_pwLocators2_get_by_text1(page:Page):
    # verify whether specific text is present on page or not

    page.goto("https://www.flipkart.com/")
    time.sleep(5)

    #Apr1:
    textEle=page.get_by_text("Select delivery location")     #Full text
    expect(textEle).to_be_visible()

    #Apr2:-
    expect(page.get_by_text("Select delivery location")).to_be_visible()   #Full Text
    expect(page.get_by_text("Select delivery")).to_be_visible()  # Partial Text


def test_verify_pwLocators2_get_by_text2_withRegularExpression(page:Page):

    page.goto("https://www.flipkart.com/")
    time.sleep(5)

    #Apr1:
    textEle=page.get_by_text(re.compile(".*Select delivery location.*"))     #Full text
    expect(textEle).to_be_visible()

    #Apr2:-
    expect(page.get_by_text("Select delivery location")).to_be_visible()    # Check Full Text
    expect(page.get_by_text("Select delivery")).to_be_visible()             # Check partial text
    expect(page.get_by_text(re.compile(".*delivery.*"))).to_be_visible()    # check Partial Text using RE
    #it Check text like before delivery and after delivery it can be anything



