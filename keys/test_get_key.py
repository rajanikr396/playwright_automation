import random
from playwright.sync_api import APIRequestContext
import pytest 
import json
file_path = "C:\\Playwright_python\\June2026_batch2_playwright_APITesting\\global_data.json"
def test_create_token(before_each_test: APIRequestContext):
      
      with open(file_path, "r") as file:
            data = json.load(file)
      payload = {
       "clientName": "Srinivas Narayan",
         "clientEmail": f"srinivas1345{random.randint(100,999)}@example{random.randint(10,99)}.com"
        }
      response = before_each_test.post("/api-clients" ,data=payload)
      assert response.status == 201
      print(json.dumps(response.json(),indent=4))
      data["accessToken"] =response.json()["accessToken"]
          # Save updated JSON
      with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
