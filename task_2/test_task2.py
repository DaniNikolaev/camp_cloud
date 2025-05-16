import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_title(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()


def test_more_info_link(page):
    page.goto("https://example.com")
    page.get_by_text("More information...").click()
    assert page.url == "https://www.iana.org/help/example-domains"
