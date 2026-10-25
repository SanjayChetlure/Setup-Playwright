import pytest
from playwright.async_api import Page, expect, async_playwright

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=False)
        mypage=await browser.new_page()

        await mypage.goto("https://www.google.com/")

        myUrl=mypage.url
        print("page url is : "+myUrl)

        await expect(mypage).to_have_url("https://www.google.com/")



# to run code using async approach
# You need to install a suitable plugin for your async framework, for example(pre-requisites):
#   - anyio
#   - pytest-asyncio  (important for async code) - pip install pytest-asyncio
#   - pytest-tornasync
#   - pytest-trio
#   - pytest-twisted


# Note- this approach we use in api testing, as we need to await for backend response,
# so we can use async approach for api testing.


