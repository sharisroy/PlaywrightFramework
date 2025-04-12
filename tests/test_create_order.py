from wsgiref import headers

import pytest
import json

# Load test data
with open("../data/credentials.json") as f:
    test_data = json.load(f)
    first_order = {"orders": [test_data["order_list"]["orders"][0]]}
    invalid_order = {"orders": [test_data["order_list"]["orders"][1]]}
@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("order", [first_order])
def test_create_order(api_context, auth_token, order):
    headers = {'Authorization': auth_token}
    # print(json.dumps(order))
    order_response = api_context.post("order/create-order", data=json.dumps(order), headers=headers)
    # print(json.dumps(order_response.json()))
    assert order_response.ok, f"Order creation failed: {order_response.text()}"
    assert order_response.json()['message'] == "Order Placed Successfully"

@pytest.mark.regression
@pytest.mark.parametrize("order", [invalid_order])
def test_create_order_invalid(api_context, auth_token, order):
    headers = {'Authorization': auth_token}
    order_response = api_context.post("order/create-order", data=json.dumps(order), headers=headers)
    # print(json.dumps(order_response.json()))
    assert order_response.json()['message'] == "Wrong Product ID"

