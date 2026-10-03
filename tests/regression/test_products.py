import pytest


@pytest.mark.regression
def test_login_regression(app_page, app_base_url):

    # Login page open
    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    # Login
    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")
    app_page.get_by_role("button", name="Login").click()

    # Login successful কিনা verify
    assert "/products" in app_page.url