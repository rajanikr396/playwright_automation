import time
import pytest
from playwright.sync_api import APIRequestContext


def test_status_24thjune2026(before_each_test: APIRequestContext):
    """GET /status using `before_each_test` base_url from conftest.py.
    Retry until successful (healing) to handle transient failures.
    """
    max_attempts = 10
    delay_seconds = 2
    expected = {"status": "UP"}

    last_status = None
    last_body = None
    for attempt in range(1, max_attempts + 1):
        response = before_each_test.get("/status")
        last_status = response.status
        try:
            last_body = response.json()
        except Exception:
            last_body = None

        if last_status == 200 and last_body == expected:
            return

        time.sleep(delay_seconds)

    pytest.fail(
        f"/status did not return {expected} after {max_attempts} attempts. "
        f"Last status={last_status}, body={last_body}"
    )
