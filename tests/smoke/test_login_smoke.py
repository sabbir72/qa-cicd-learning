import pytest


@pytest.mark.smoke
def test_login_success(app_page, app_base_url):

    # Login page open
    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    # Enter username
    app_page.locator("//input[@placeholder='Username']").fill("admin")

    # Enter password
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    # Click Login
    app_page.get_by_role("button", name="Login").click()

    # Products page verify
    app_page.get_by_role(
        "heading",
        name="Products",
        exact=True
    ).wait_for()

    # URL verify
    assert "/products" in app_page.url


@pytest.mark.smoke
def test_logout_success(app_page, app_base_url):

    # Login
    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    app_page.get_by_role("button", name="Login").click()

    # Products page
    app_page.get_by_role(
        "heading",
        name="Products",
        exact=True
    ).wait_for()

    # Logout
    app_page.get_by_role("link", name="Logout").click()

    # Login page verify
    app_page.get_by_role(
        "heading",
        name="Login",
        exact=True
    ).wait_for()

    # URL verify
    assert "/login" in app_page.url