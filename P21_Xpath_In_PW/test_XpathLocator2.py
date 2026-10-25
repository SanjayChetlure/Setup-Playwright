import time

import pytest
from playwright.sync_api import Page,expect

def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    products=page.locator("//a[contains(text(),'Computers')]")

    #check total, o of products
    print(products.count())
    expect(products).to_have_count(3)
    time.sleep(5)

    # text_content()  -> it is like getText in selenium
    #capture 1st element text
    firstCompText =products.first.text_content()     #return text of single element
    print("firstCompText: "+firstCompText)

    #capture 1st element text
    lastCompText =products.last.text_content()
    print("lastCompText: "+lastCompText)

    # capture nth element text
    nthCompText = products.nth(2).text_content()       #Index start from 0
    print("nthCompText: " + nthCompText)

    #print all product text - using looping stat
    print("-----")
    allProductTexts=products.all_text_contents()   #returns text of multiple products
    print(allProductTexts)
    print("-----")
    for i in allProductTexts:
        print(i)

    # products is locator type of object & nth, first,last & nth are related to locator object
    # text_content()  # return text of single element
    # all_text_contents()  # returns text of multiple products

