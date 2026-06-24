import json
from pathlib import Path
from playwright.sync_api import APIRequestContext
import pytest
file_path = "C:\\Playwright_python\\June2026_batch2_playwright_APITesting\\global_data.json"
@pytest.mark.dependency(scope="session", depends=["add_item_to_cart"])
@pytest.mark.order(3)
def test_delete_an_item(before_each_test: APIRequestContext):
    # Load existing JSON data
    with open(file_path, "r") as file:
        data = json.load(file)
    cart_id = data.get("cart_id")
    assert cart_id is not None, "Missing cart_id in global_data.json; create a cart first."
    items = data.get("item_id", [])
    assert items, "No item_id entries in global_data.json to delete."
    # Delete the most recently added item
    item_id = items.pop()
    response = before_each_test.delete(f"/carts/{cart_id}/items/{item_id}")
    assert response.status in (200, 204), f"Unexpected status {response.status}: {response.text()}"
    # Persist updated item list
    data["item_id"] = items
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Deleted Item ID: {item_id} (status: {response.status})")
