import json
import pytest
from playwright.sync_api import APIRequestContext
file_path = r"C:\Playwright_python\June2026_batch2_playwright_APITesting\global_data.json"
@pytest.mark.dependency(scope="session", name="add_item_to_cart", depends=["create_cart"])
@pytest.mark.order(2)
@pytest.mark.parametrize("pid", [1225, 1709, 1710])
def test_add_an_item_to_cart(before_each_test: APIRequestContext, pid):
   # Load existing JSON data
   with open(file_path, "r") as file:
       data = json.load(file)
   cart_id = data.get("cart_id")
   payload = {
       "productId": pid,
       "quantity": 2
   }
   response = before_each_test.post(
       f"/carts/{cart_id}/items",
       data=payload
   )
   assert response.status == 201
   print(json.dumps(response.json(), indent=4))
   item_id = response.json()["itemId"]
   data["item_id"].append(item_id)
   with open(file_path, "w") as file:
       json.dump(data, file, indent=4)




