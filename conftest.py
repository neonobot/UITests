import json
from pathlib import Path
from typing import Generator

import pytest
from playwright.sync_api import Playwright, BrowserContext, Page

from serviceCalls.helper import password


@pytest.fixture()
def context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    path_to_extension = Path(__file__).parent.joinpath(
        "serviceCalls/chromium_profile/Profile 1/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.32.0_0")
    user_profile = "serviceCalls/chromium_profile"
    context = playwright.chromium.launch_persistent_context(
        user_profile,
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    yield context
    context.close()


@pytest.fixture()
def extension_id(context) -> Generator[str, None, None]:
    # for manifest v2:
    background = context.background_pages[0]
    if not background:
        background = context.wait_for_event("backgroundpage")

    extension_id = background.url.split("/")[2]
    yield extension_id


@pytest.fixture()
def metamask_signin(page: Page, extension_id: str):
    page.goto(f"chrome-extension://{extension_id}/home.html#onboarding/welcome")
    page.context.pages[2].close()
    page.context.pages[0].close()
    page.locator('input[id = "password"]').fill(password)
    page.locator('[data-testid="unlock-submit"]').click()
    # page.locator('[data-testid="onboarding-terms-checkbox"]').click()
    # page.get_by_test_id("onboarding-import-wallet").click()
    # page.locator('[data-testid="metametrics-i-agree"]').click()
    # page.locator('#import-srp__srp-word-0').click()
    # pyperclip.copy(secret_phrase)
    # page.locator('#import-srp__srp-word-0').press('Meta+V')
    # page.locator('#import-srp__srp-word-0').press('Enter')
    # page.locator('[data-testid="import-srp-confirm"]').click()
    # page.locator('[data-testid="create-password-new"]').fill(password)
    # page.locator('[data-testid="create-password-confirm"]').fill(password)
    # page.locator('[data-testid="create-password-terms"]').click()
    # page.locator('button[data-testid="create-password-import"]').click()
    # page.locator('button[data-testid="onboarding-complete-done"]').click()
    # page.locator('button[data-testid="pin-extension-next"]').click()
    # page.locator('button[data-testid="pin-extension-done"]').click()
    # page.locator('button[data-testid="popover-close"]').click()
    return page



