import pytest


@pytest.mark.regression
def test_valid_login(app_page, app_base_url):

    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    app_page.get_by_role("button", name="Login").click()

    # Products page verify
    app_page.get_by_role(
        "heading",
        name="Products",
        exact=True
    ).wait_for()

    assert "/products" in app_page.url


@pytest.mark.regression
def test_invalid_username(app_page, app_base_url):

    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("wronguser")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    app_page.get_by_role("button", name="Login").click()

    assert app_page.get_by_text(
        "Invalid username or password"
    ).is_visible()


@pytest.mark.regression
def test_invalid_password(app_page, app_base_url):

    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("wrongpass")

    app_page.get_by_role("button", name="Login").click()

    assert app_page.get_by_text(
        "Invalid username or password"
    ).is_visible()


@pytest.mark.regression
def test_products_after_login(app_page, app_base_url):

    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    app_page.get_by_role("button", name="Login").click()

    # Products page verify
    app_page.get_by_role(
        "heading",
        name="Products",
        exact=True
    ).wait_for()

    # Product list verify
    assert app_page.get_by_text("Laptop").is_visible()
    assert app_page.get_by_text("Mouse").is_visible()
    assert app_page.get_by_text("Keyboard").is_visible()


@pytest.mark.regression
def test_products_without_login(app_page, app_base_url):

    app_page.goto(f"{app_base_url.rstrip('/')}/products")

    app_page.get_by_role(
        "heading",
        name="Login",
        exact=True
    ).wait_for()

    assert "/login" in app_page.url


@pytest.mark.regression
def test_logout(app_page, app_base_url):

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

    assert "/login" in app_page.url


@pytest.mark.regression
def test_access_products_after_logout(app_page, app_base_url):

    # Login
    app_page.goto(f"{app_base_url.rstrip('/')}/login")

    app_page.locator("//input[@placeholder='Username']").fill("admin")
    app_page.locator("//input[@placeholder='Password']").fill("admin123")

    app_page.get_by_role("button", name="Login").click()

    # Logout
    app_page.get_by_role("link", name="Logout").click()

    # Try to access Products after logout
    app_page.goto(f"{app_base_url.rstrip('/')}/products")

    # Should redirect to Login
    app_page.get_by_role(
        "heading",
        name="Login",
        exact=True
    ).wait_for()

    assert "/login" in app_page.url