import pytest
import json

# Load test data
with open("../data/credentials.json") as f:
    test_data = json.load(f)

@pytest.mark.regression
@pytest.mark.parametrize("user_credentials", test_data["user_credentials"])
def test_login(api_context, user_credentials):
    response = api_context.post("auth/login", data=user_credentials)
    assert response.ok, f"Login failed: {response.text()}"
    response_json = response.json()
    assert "token" in response_json, "Token not found in response"
    # print(f"Login successful! Token: {response_json['token']}")
