from playwright.sync_api import Playwright
base_url ="https://simple-grocery-store-api.click"
def test_status(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get(f"{base_url}/status")
    print (f"status code ={response.status}")
    assert response.status == 200
    print (response.json())
    assert response.json()['status'] == 'UP'
    print ("--------------Headers--------------------------")
    print( response.headers)
    assert response.headers['content-type'] == 'application/json'
