import os
import pytest
from playwright.sync_api import Page


@pytest.fixture
def app_base_url():
    """
    QA application Base URL.

    Local testing:
    BASE_URL=http://127.0.0.1:5000

    CI/CD testing:
    BASE_URL will come from GitHub Actions.

    Default:
    Vercel deployed Developer application
    """

    return os.getenv(
        "BASE_URL",
        "https://developer-demo-app.vercel.app/"
    )


@pytest.fixture
def app_page(page: Page, app_base_url):
    """
    Open the Developer application
    before each test.
    """

    page.goto(app_base_url)

    return page