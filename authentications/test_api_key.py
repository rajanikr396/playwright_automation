import json
from playwright.sync_api import Playwright


def test_api_key_auth(playwright: Playwright):
    # Replace with a secure secret retrieval in CI (do not hardcode tokens)
    api_key = "GITHUB_PAT_PLACEHOLDER"
    request = playwright.request.new_context()
    response = request.get(
        "https://api.github.com/user/repos",
        headers={
            "Authorization": f"Bearer {api_key}"
        }
    )
    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
    request.dispose()
