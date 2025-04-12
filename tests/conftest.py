import datetime

import pytest
import json

from playwright.sync_api import Playwright

# Load Config
with open("../config/config.json") as f:
    config = json.load(f)

BASE_URL = config["base_url"]
HEADERS = config["headers"]

# Load User Credentials
with open("../data/credentials.json") as f:
    test_data = json.load(f)
USER_CREDENTIALS = test_data["user_credentials"][0]  # Use first user

@pytest.fixture(scope="module")
def api_context(playwright: Playwright):
    # Fixture for setting up Playwright request context.
    request_context = playwright.request.new_context(base_url=BASE_URL, extra_http_headers=HEADERS)
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="module")
def auth_token(api_context):
    response = api_context.post("auth/login", data=USER_CREDENTIALS)
    assert response.ok, f"Login failed: {response.text()}"
    token = response.json().get("token")
    assert token, "Token not found in response"
    return token


@pytest.fixture(scope="module")
def latest_order_id(api_context, auth_token):
    headers = {'Authorization': auth_token}
    order_response = api_context.get("order/get-orders-for-customer/67d8f80dc019fb1ad62b991d", headers=headers)
    assert order_response.json()['message'] == "Orders fetched for customer Successfully"
    latest_order_id = order_response.json()['data'][0]['_id']
    return latest_order_id


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not hasattr(config, "metadata"):  # Ensure metadata exists
        config.metadata = {}

    config.metadata["Project"] = "E2E API Automation"
    config.metadata["Tester"] = "Haris"
    config.metadata["Execution Time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # print(f"✅ Metadata Updated: {config.metadata}")


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Custom API Test Report"


# def test_hh():
#     print(f"BASE_URL: {BASE_URL}")