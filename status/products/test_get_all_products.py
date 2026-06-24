import json
from playwright.sync_api import Playwright
base_url ="https://simple-grocery-store-api.click"
def test_get_all_products(playwright: Playwright):
       request  = playwright.request.new_context()
       response  = request.get(
              f"{base_url}/products",
              params={ "category":"meat-seafood", "results":2 ,"available":"true"}
              
              )
       assert response.status == 200
       print (json.dumps(response.json(),indent=4))
