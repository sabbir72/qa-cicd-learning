import pytest


@pytest.mark.smoke
def test_login_success(app_page, app_base_url):
    # Login page open
    app_page.goto(f"{app_base_url.rstrip('/')}")

    # Username
    app_page.locator("//input[@placeholder='Username']").fill("admin")

    # Password
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    # Login button
    app_page.get_by_role("button", name="Login").click()

    # Verify successful login
    app_page.get_by_role("heading", name="Products").wait_for()

    # Verify URL
    assert "/products" in app_page.url