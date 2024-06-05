def test_login_with_valid_creds(login_page, inventory_page, username='standard_user', password='secret_sauce'):
    login_page.login(username, password)
    assert inventory_page.is_product_title_visible(), "Inventory page title not found"
    assert inventory_page.get_product_title_text() == "Products", "Inventory page title text is incorrect"


def test_login_with_no_creds(login_page, username="", password=""):
    login_page.login(username, password)
    assert login_page.is_error_message_visible(), "Error message does not occur"
    assert login_page.get_error_mess_text() == "Epic sadface: Username is required", "Error message text is incorrect"
