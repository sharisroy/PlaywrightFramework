import pytest
@pytest.mark.regression
@pytest.mark.smoke
def test_get_all_orders(api_context, auth_token):
    headers = {'Authorization': auth_token}
    order_response = api_context.get("order/get-orders-for-customer/67d8f80dc019fb1ad62b991d", headers=headers)
    assert order_response.json()['message'] == "Orders fetched for customer Successfully"
    # print(order_response.json())

