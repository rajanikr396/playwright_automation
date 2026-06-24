import pytest
from playwright.sync_api import Playwright
BASE_URL = "https://simple-grocery-store-api.glitch.me"
@pytest.fixture(scope="function")
def before_each_test(playwright: Playwright):
   request_context = playwright.request.new_context(
       base_url=BASE_URL
   )
   yield request_context
   request_context.dispose()
