from playwright.sync_api import Playwright, expect


# def test_go_to_gmail_from_google(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.com/gmail/about/")
#     page.goto(
#         "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com"
#         "%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp")
#     page.locator("#firstName").type("Нана")
#     page.locator("#lastName").type("Скворцова")
#     page.locator("#lastName").press("Enter")
#     page.locator("#day").click()
#     page.locator("#day").type("21")
#     page.locator("#month").click()
#     page.select_option("#month", value="4")
#     page.locator("#year").click()
#     page.locator("#year").type("2000")
#     page.locator("#gender").click()
#     page.select_option("#gender", value="2")
#     page.locator("#birthdaygenderNext").click()
#     page.locator("#selectionc2").click()
#     page.locator('input[name="Username"]').click()
#     page.locator('input[name="Username"]').type("neorodeo008")
#     page.locator("#next").click()
#     page.locator('input[name="Passwd"]').click()
#     page.locator('input[name="Passwd"]').type("Betman007/")
#     page.locator('input[name="PasswdAgain"]').click()
#     page.locator('input[name="PasswdAgain"]').type("Betman007/")
#     page.locator("#createpasswordNext").click()
#     page.locator('[jsname="uRHG6"]').click()
#     page.locator('[jsname="uRHG6"]').click()
#     page.locator("#next").click()
#     page.locator('[jsname="Njthtb"]').click()


# def test_drag_and_drop(page):
#    page.goto('https://draganddrop.antonzimaiev.repl.co/')
#    page.drag_and_drop("#drag", "#drop")


def test_delete_draft(playwright: Playwright, new_draft) -> None:
    page = new_draft
    page.drag_and_drop('(//div[@class="Cp"]//table//tr)[1]', '[data-tooltip="Корзина"]')
    page.locator('[data-tooltip="Корзина"]').click()
    expect(page.locator('//div[@class="Cp"]//table//tr')).not_to_be_visible()
