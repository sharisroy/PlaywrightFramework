import json

from playwright.sync_api import Playwright, APIRequestContext
import pytest

base_url = "https://rahulshettyacademy.com/api/ecom/"
# login_data = {"userEmail": "sqa.haris@gmail.com", "userPassword": "H@12345bd"}

with open('../data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_api(playwright: Playwright, user_credentials):
    request_context = playwright.request.new_context(base_url=base_url)
    response = request_context.post("auth/login",
                                    data=user_credentials)
    print(response.json())
    print(response.json()["token"])

    assert response.ok
