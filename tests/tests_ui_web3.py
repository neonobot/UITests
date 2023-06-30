from playwright.sync_api import Page

from serviceCalls.helper import screenshot_comparison
from serviceCalls.web3_service import MainPage, SendPage, MetamaskPage


# def test_popup_page(page: Page, metamask_signin, extension_id: str) -> None:
# page.goto("https://zomet-dev.3ahtim54r.ru/#/main")
# page.get_by_text('MetaMask').nth(0).click()
# page.goto(f"chrome-extension://{extension_id}/popup.html")
# page.locator('button[class="button btn--rounded btn-primary"]').click() # Клик на кнопку "Далее"
# page.locator('button[data-testid="page-container-footer-next"]').click() # Подключиться
# page.goto("https://zomet-dev.3ahtim54r.ru/#/main")
# page.get_by_text('MetaMask').nth(0).click()
# Продолжение действий на основной странице
# page.locator('[href="#/send"]').click()


def test_mocking_blockchain(page: Page, metamask_signin, extension_id: str) -> None:
    # сравнение скриншотов и мокирование запросов на главной странице
    MainPage(page).handle_route()
    MainPage(page).go_to()
    page.wait_for_load_state('networkidle')
    page.screenshot(path='main_screenshot.png', full_page=True)
    screenshot_comparison(base_image='basic_main_screenshot.png', test_image='main_screenshot.png')


def test_mock_transaction(page: Page, metamask_signin, extension_id: str) -> None:
    SendPage(page).go_to()
    SendPage(page).network_selection(extension_id)
    SendPage(page).go_to()
    SendPage(page).send_transaction()
    page.wait_for_load_state('networkidle')
    MetamaskPage(extension_id=extension_id, page=page).confirm_transaction_notification()
