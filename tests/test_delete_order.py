import pytest

@pytest.mark.smoke
def test_delete_order(api_context, auth_token, latest_order_id):
    headers = {'Authorization': auth_token}
    path = f'order/delete-order/{latest_order_id}'
    delete_order = api_context.delete(path, headers=headers)
    assert delete_order.json()['message'] == "Orders Deleted Successfully"


@pytest.mark.skip(reason="Not Implemented")
def test_invalid_delete_order(api_context, auth_token, latest_order_id):
    headers = {'Authorization': auth_token}
    path = f'order/delete-order/67dba912c019fb1ad62f8b2b'
    delete_order = api_context.delete(path, headers=headers)
    assert delete_order.json()['message'] == "Order not found"
