import pytest
import json

# Load test data from credentials.json
def load_test_data():
    with open("../data/credentials.json") as f:
        return json.load(f)

# Separate valid and invalid users
def get_valid_users():
    test_data = load_test_data()
    return [user for user in test_data["user_credentials"] if user["userPassword"] == "H@12345bd"]

def get_invalid_users():
    test_data = load_test_data()
    return [user for user in test_data["user_credentials"] if user["userPassword"] != "H@12345bd"]

# Helper function to generate ids (to show in report)
def id_func(user_credentials):
    return f"{user_credentials['userEmail']}|{user_credentials['userPassword']}"

# ✅ Test for Valid Login
@pytest.mark.regression
@pytest.mark.parametrize("user_credentials", get_valid_users(), ids=lambda x: id_func(x))
def test_valid_login(api_context, user_credentials):
    """
    Test login with valid credentials.
    Expect status 200 and token present.
    """
    response = api_context.post("auth/login", data=user_credentials)
    response_json = response.json()

    assert response.status == 200, f"Expected 200 OK but got {response.status}"
    assert "token" in response_json, "Expected token not found in response"
    print(f"✅ Valid Login successful! Token: {response_json['token']}")

# ✅ Test for Invalid Login
@pytest.mark.regression
@pytest.mark.parametrize("user_credentials", get_invalid_users(), ids=lambda x: id_func(x))
def test_invalid_login(api_context, user_credentials):
    """
    Test login with invalid credentials.
    Expect failure status and no token.
    """
    response = api_context.post("auth/login", data=user_credentials)
    response_json = response.json()

    assert response.status != 200, f"Expected login failure but got success with {response.status}"
    assert "token" not in response_json, "Token should not be present for invalid login"
    print(f"❌ Invalid Login failed as expected: {response.text()}")
