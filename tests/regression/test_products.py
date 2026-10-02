import pytest


@pytest.mark.regression
def test_products_page_after_login(app_page, app_base_url):
    # Login page open
    app_page.goto(f"{app_base_url.rstrip('/')}")

    # Login
    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")
    app_page.get_by_role("button", name="Login").click()

    # Products page verify
    app_page.get_by_role("heading", name="Products").wait_for()

    # Product names verify
    assert app_page.get_by_text("Laptop").is_visible()
    assert app_page.get_by_text("Mouse").is_visible()
    assert app_page.get_by_text("Keyboard").is_visible()