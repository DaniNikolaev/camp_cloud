import pytest
from playwright.sync_api import expect, sync_playwright


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_title(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")


def test_more_info_link(page):
    page.goto("https://example.com")
    page.get_by_text("More information...").click()
    expect(page).to_have_url("https://www.iana.org/help/example-domains")
