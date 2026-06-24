import base64
from playwright.sync_api import Playwright
def test_basic_auth(playwright: Playwright):
    
    credentials =base64.b64encode(b"admin:admin").decode("utf-8")
    request  = playwright.request.new_context()
    response = request.get(
             "http://the-internet.herokuapp.com/basic_auth",
             headers={
                 "Authorization": f"Basic {credentials}"
             }
    )
    assert response.status == 200
    response_text = response.text()
    print("Response Text:", response_text)
