from playwright.sync_api import Page

from serviceCalls.helper import handle_route_balance, handle_route_tokens_version_by_eth, \
    handle_route_tokens_version_by_bsc, handle_route_tokens_version_by_polygon, handle_route_tokens_version_by_arbitrum, \
    handle_route_tokens_version_by_avalanche, handle_route_tokens_version_by_optimism, keys_data, wallet, \
    intercept_request


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = ''

    def go_to(self):
        self.page.goto(self.url)


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://zomet-dev.3ahtim54r.ru/#/main'

    def handle_route(self):
        networks = list(keys_data().keys())
        for network in networks:
            net = keys_data()[network].get('net')
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/{net}/{wallet}/balance",
                            handle_route_balance)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/eth/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_eth)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/bsc/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_bsc)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/polygon/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_polygon)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/arbitrum/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_arbitrum)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/avalanche/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_avalanche)
            self.page.route(f"https://api.3ahtim54r.ru/blockchain/optimism/{wallet}/tokens?version=1.1.0",
                            handle_route_tokens_version_by_optimism)


class SendPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://zomet-dev.3ahtim54r.ru/#/send'

    def network_selection(self, extension_id):
        self.page.select_option('[class="flex justify-center items-center pointer minimized_ac svelte-1uqued6"]',
                                value="0x38")
        self.page.goto(f"chrome-extension://{extension_id}/popup.html")
        button = self.page.query_selector('button[class="button btn--rounded btn-primary"]')
        if button:
            button.click()

    def send_transaction(self):
        self.page.locator('input[class="input-address"]').fill(wallet)
        self.page.locator('div.token').click()
        self.page.get_by_text('Oleg 🍔').click()
        self.page.locator('input.input-balance').fill('0.001')
        self.page.locator('input.input-balance').press('Enter')
        self.page.get_by_text('CONFIRM').click()


class MetamaskPage(BasePage):
    def __init__(self, page: Page, extension_id):
        super().__init__(page)
        self.url = f"chrome-extension://{extension_id}/popup.html"

    def confirm_transaction_notification(self):
        self.page.on("request", lambda request: print(">>", request.method, request.url))
        self.page.on("response", lambda response: print("<<", response.status, response.url))
        self.page.goto(self.url)
        self.page.route('**/*', intercept_request)
        self.page.wait_for_load_state('networkidle')
        # self.page.locator('button[data-testid="page-container-footer-next"]').click()
